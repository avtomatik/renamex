mod clean;
mod cli;
mod constants;
mod error;
mod file_ops;
mod filter;
mod transform;

use tracing_subscriber::{EnvFilter, fmt};

fn main() {
    fmt().with_env_filter(EnvFilter::from_default_env()).init();

    if let Err(e) = cli::run() {
        eprintln!("Error: {}", e);
        std::process::exit(1);
    }
}
