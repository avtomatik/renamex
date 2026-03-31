mod cli;
mod file_ops;
mod transform;
mod clean;
mod filter;
mod constants;

fn main() {
    if let Err(e) = cli::run() {
        eprintln!("Error: {}", e);
    }
}
