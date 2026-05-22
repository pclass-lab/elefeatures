from importlib.metadata import version, PackageNotFoundError, metadata
import logging
import typer

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
    help="mcce-features: Extract electrostatic features from MCCE output files or other sources.",
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
    """Extract electrostatic features from a MCCE working directory."""
    core.extract(mcce_folder)

@app.command("extract-folders")
def extract_folders_cmd(
    folder_file: str = typer.Argument(
        ...,
        help=("Path to a (space, comma, tab) delimited file with a "
              "MCCE folder path/str in the first column of each line.")
                                      ),
    output_file: str = typer.Option("mcce_elefeatures.tsv",
                                    help="Path to the output TSV file.")
):
    """Extract electrostatic features from multiple MCCE folders."""
    core.extract_folders(folder_file, output_file)
