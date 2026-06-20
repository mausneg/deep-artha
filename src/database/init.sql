-- DeepArtha Database Initialization Script
-- Phase 2: Database Infrastructure

-- Enable pgvector extension for RAG capabilities
CREATE EXTENSION IF NOT EXISTS vector;

-- 1. Categories Table
-- Stores categories for expenditures and assets (e.g., 'Food', 'Investment', 'Rent')
CREATE TABLE IF NOT EXISTS kategori (
    id SERIAL PRIMARY KEY,
    nama VARCHAR(100) NOT NULL UNIQUE,
    deskripsi TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Expenditures Table
-- Records all spending. Supports RAG via embedding for receipt analysis.
CREATE TABLE IF NOT EXISTS pengeluaran (
    id SERIAL PRIMARY KEY,
    tanggal DATE NOT NULL,
    jumlah DECIMAL(15, 2) NOT NULL,
    kategori_id INTEGER REFERENCES kategori(id),
    deskripsi TEXT,
    nota_url TEXT, -- URL to the image stored in Telegram/Cloud
    embedding vector(1536), -- Embedding for RAG (assuming OpenAI/Claude size)
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Portfolio Table
-- Tracks assets and their values
CREATE TABLE IF NOT EXISTS portofolio (
    id SERIAL PRIMARY KEY,
    nama_aset VARCHAR(255) NOT NULL,
    simbol_ticker VARCHAR(20), -- e.g., 'AAPL', 'BTC', 'BBCA.JK'
    jumlah_unit DECIMAL(18, 8) NOT NULL,
    harga_rata_rata DECIMAL(15, 2),
    kategori_id INTEGER REFERENCES kategori(id),
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Seed basic categories
INSERT INTO kategori (nama, deskripsi) VALUES 
('Makanan & Minuman', 'Pengeluaran harian untuk konsumsi'),
('Transportasi', 'Bensin, Grab, Gojek, Parkir'),
('Investasi', 'Saham, Crypto, Reksa Dana'),
('Kesehatan', 'Obat, Dokter, Gym'),
('Utilitas', 'Listrik, Air, Internet, Pulsa'),
('Lain-lain', 'Pengeluaran yang tidak masuk kategori utama')
ON CONFLICT (nama) DO NOTHING;

-- Create indices for performance
CREATE INDEX IF NOT EXISTS idx_pengeluaran_tanggal ON pengeluaran(tanggal);
CREATE INDEX IF NOT EXISTS idx_pengeluaran_kategori ON pengeluaran(kategori_id);
CREATE INDEX IF NOT EXISTS idx_portofolio_ticker ON portofolio(simbol_ticker);
