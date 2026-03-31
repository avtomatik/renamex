use clap::Parser;
use std::path::PathBuf;

use crate::file_ops::process_files;
use crate::filter::extension_filter;

#[derive(Parser)]
pub struct Args {
    #[arg(default_value = ".")]
    path: PathBuf,

    #[arg(short, long)]
    extensions: Vec<String>,

    #[arg(short, long)]
    verbose: bool,
}

pub fn run() -> Result<(), Box<dyn std::error::Error>> {
    let args = Args::parse();

    let filter = if args.extensions.is_empty() {
        None
    } else {
        Some(extension_filter(args.extensions))
    };

    process_files(&args.path, filter.as_ref(), args.verbose)?;

    Ok(())
}
