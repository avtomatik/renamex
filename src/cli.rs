use clap::Parser;
use std::path::PathBuf;

use crate::error::AppError;
use crate::file_ops::process_files;
use crate::filter::extension_filter;

#[derive(Parser, Debug)]
#[command(name = "fileworks")]
pub struct Args {
    #[arg(default_value = ".")]
    pub path: PathBuf,

    #[arg(short, long)]
    pub extensions: Vec<String>,

    #[arg(short, long)]
    pub verbose: bool,

    #[arg(long)]
    pub dry_run: bool,
}

pub fn run() -> Result<(), AppError> {
    let args = Args::parse();

    if !args.path.is_dir() {
        return Err(AppError::InvalidDirectory(args.path.display().to_string()));
    }

    let filter = if args.extensions.is_empty() {
        None
    } else {
        Some(extension_filter(args.extensions))
    };

    process_files(&args.path, filter.as_ref(), args.verbose, args.dry_run)?;

    Ok(())
}
