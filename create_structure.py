import os

# Define the folder structure
project_structure = {
    "config": ["config.json", "database_config.json", "strategies_config.json", "logging_config.json"],
    "data": ["raw/", "processed/", "database/", "data_collector.py", "data_cleaner.py", "database_manager.py"],
    "ml_models": [
        "model_trainer.py", "model_predictor.py", "feature_engineering.py", "ml_utils.py",
        "models/", "strategies_ml/", "strategies_ml/ml_strategy_base.py", "strategies_ml/ml_regression.py",
        "strategies_ml/ml_classification.py", "strategies_ml/reinforcement_learning.py"
    ],
    "strategies": ["base_strategy.py", "moving_average.py", "mean_reversion.py", "momentum_strategy.py"],
    "backtesting": ["backtester.py", "performance_metrics.py", "visualization.py"],
    "execution": [
        "broker_interface.py", "live_execution.py", "paper_trading.py", "exchanges/",
        "exchanges/binance_api.py", "exchanges/ibkr_api.py"
    ],
    "monitoring": ["dashboard_app.py", "performance_dashboard.py", "logger_visualizer.py", "trade_monitor.py"],
    "utils": ["logger.py", "indicators.py", "helpers.py", "notifier.py"],
    "tests": ["test_data_collector.py", "test_backtester.py", "test_ml_models.py", "test_execution.py"],
    "notebooks": ["strategy_analysis.ipynb", "ml_training.ipynb", "feature_engineering.ipynb"],
    "docs": ["project_overview.md", "module_details.md", "api_documentation.md"],
}

# Files in root directory
root_files = ["README.md", "requirements.txt", "setup.py", ".gitignore", "LICENSE", "main.py"]

def create_structure(base_path="algo_trading_project"):
    # Create base directory
    os.makedirs(base_path, exist_ok=True)
    print(f"Created project directory: {base_path}")

    # Create subdirectories and files
    for folder, files in project_structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")
        for file in files:
            if file.endswith("/"):  # If it's a subdirectory
                os.makedirs(os.path.join(folder_path, file), exist_ok=True)
                print(f"Created subfolder: {os.path.join(folder_path, file)}")
            else:
                file_path = os.path.join(folder_path, file)
                open(file_path, 'w').close()
                print(f"Created file: {file_path}")

    # Create root-level files
    for file in root_files:
        file_path = os.path.join(base_path, file)
        open(file_path, 'w').close()
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    create_structure()
