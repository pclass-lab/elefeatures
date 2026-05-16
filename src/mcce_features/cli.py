import logging
import typer
from importlib.metadata import version, PackageNotFoundError, metadata
from . import core

try:
    __version__ = version("mcce-features")
    meta = metadata("mcce-features")
    __email__ = meta.get("Author-email", "unknown")
except PackageNotFoundError:
    __author__ = "unknown"
    __email__ = "unknown"
    __version__ = "unknown"


def print_version():
    typer.echo(f"mcce-features version: {__version__}")
    typer.echo(f"mcce-features developer: {__email__}")


app = typer.Typer(
    help="mcce-features: extract electrostatic features from MCCE output files or other sources.",
    context_settings={"help_option_names": ["-h", "--help"]},
    no_args_is_help=True
)

# -----------------------------
# Logging setup
# -----------------------------
def setup_logging(level: str = "INFO"):
    """Configure root logger with simple text format."""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="[%(levelname)s]: %(message)s",
    )


# -----------------------------
# Global callback
# -----------------------------
@app.callback()
def main(
    log_level: str = typer.Option(
        "INFO",
        "--log-level",
        "-l",
        help="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)"
    )
):
    """Configure logging before running any command."""
    setup_logging(log_level)

# -----------------------------
# Global version command
# -----------------------------
@app.command("version")
def version_cmd():
    """Show mcce-features version."""
    print_version()


@app.command("extract")
def extract(
    mcce_folder: str = typer.Argument(..., help="Path to the MCCE working directory.")
):
    """Extract electrostatic features from MCCE working directory."""
    core.extract(mcce_folder)
