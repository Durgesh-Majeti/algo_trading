CREATE TABLE stocks (
    stock_id SERIAL PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    company_name VARCHAR(255),
    sector VARCHAR(100),
    industry VARCHAR(100),
    isin VARCHAR(12),
    exchange VARCHAR(50),
    currency VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a trigger function to update the `updated_at` column
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create the trigger to fire before any row is updated
CREATE TRIGGER set_updated_at
BEFORE UPDATE ON stocks
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TABLE historical_data (
    record_id SERIAL PRIMARY KEY,
    stock_id INTEGER REFERENCES stocks(stock_id),
    date DATE NOT NULL,
    open_price DECIMAL(15, 2),
    high_price DECIMAL(15, 2),
    low_price DECIMAL(15, 2),
    close_price DECIMAL(15, 2),
    volume BIGINT,
    adjusted_close DECIMAL(15, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE intraday_data (
    record_id SERIAL PRIMARY KEY,
    stock_id INTEGER REFERENCES stocks(stock_id),
    timestamp TIMESTAMP NOT NULL,
    price DECIMAL(15, 2),
    volume BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE corporate_actions (
    action_id SERIAL PRIMARY KEY,
    stock_id INTEGER REFERENCES stocks(stock_id),
    action_type VARCHAR(50),
    action_date DATE,
    value DECIMAL(15, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE financials (
    record_id SERIAL PRIMARY KEY,
    stock_id INTEGER REFERENCES stocks(stock_id),
    year SMALLINT CHECK (year >= 1900 AND year <= 2100)
    revenue DECIMAL(15, 2),
    net_profit DECIMAL(15, 2),
    eps DECIMAL(15, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE indices (
    index_id SERIAL PRIMARY KEY,
    index_name VARCHAR(100),
    date DATE NOT NULL,
    open_price DECIMAL(15, 2),
    high_price DECIMAL(15, 2),
    low_price DECIMAL(15, 2),
    close_price DECIMAL(15, 2),
    volume BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);