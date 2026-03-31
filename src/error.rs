use thiserror::Error;

#[derive(Error, Debug)]
pub enum AppError {
    #[error("Invalid directory: {0}")]
    InvalidDirectory(String),

    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
}
