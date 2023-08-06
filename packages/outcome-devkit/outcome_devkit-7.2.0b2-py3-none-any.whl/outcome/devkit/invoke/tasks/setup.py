import platform
from typing import Dict, Optional

from invoke import Collection, Context, run, task
from outcome.read_toml import lib as read_toml
from outcome.utils.env import is_ci

from outcome.devkit.invoke import app, env


@env.add
def build_system_requirements(e: env.Env) -> Optional[str]:
    return read_toml.read_from_file(env.r(app.pyproject_file), 'build-system.requires')


@env.add
def poetry_ld_flags_from_brew(e: env.Env) -> str:
    # Retrieve the path to the ssl library, used for compiling some python C extensions
    path: str = run('brew --prefix openssl', echo=False, hide=True).stdout
    return f'-L{path.strip()}/lib'


@task
def build_system(c: Context, skip_pre_commit: bool = False):
    """Install essential build system components."""
    requirements = env.r(build_system_requirements)
    c.run(f'pip install "{requirements}"')

    info = app.get_git_info()

    if not is_ci() and not skip_pre_commit and info is not None:
        # Setup pre-commit
        c.run('pre-commit install -t pre-commit')
        c.run('pre-commit install -t pre-push')
        c.run('pre-commit install -t commit-msg')


@task
def install_pyright(c: Context, version: str = '1.1.135'):
    """Install Pyright (specific version)"""

    c.run(f'npm i -g pyright@{version}')


@task(build_system, install_pyright)
def ci(c: Context):
    """Install the dependencies for CI environments."""
    c.run('poetry install --no-interaction --no-ansi --remove-untracked')


@task(build_system, install_pyright)
def dev(c: Context):
    """Install the dependencies for dev environments."""
    install_env: Dict[str, str] = {}

    if platform.system() == 'Darwin':
        install_env.update({'LDFLAGS': env.r(poetry_ld_flags_from_brew)})

    c.run('poetry install --remove-untracked', env=install_env)


@task(build_system)
def production(c: Context):
    """Install the dependencies for production environments."""
    c.run('poetry config virtualenvs.create true')
    c.run('poetry config virtualenvs.in-project true')
    c.run('poetry install --no-dev --no-interaction --no-ansi  --remove-untracked')


@task
def auto(c: Context):
    """Install either dev or CI dependencies, based on the environment."""
    if is_ci():
        ci(c)
    else:
        dev(c)


namespace = Collection(build_system, install_pyright, ci, dev, production, auto)
