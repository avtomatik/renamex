mod clean;
mod cli;
mod constants;
mod error;
mod file_ops;
mod filter;
mod transform;

fn main() {
    tracing_subscriber::fmt::init();

    if let Err(e) = cli::run() {
        eprintln!("Error: {}", e);
        std::process::exit(1);
    }
}
