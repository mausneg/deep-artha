## Roadmap & TODO List (DeepArtha)

Berikut adalah tahapan pengembangan proyek **DeepArtha** yang dibagi menjadi beberapa fase inkremental.
,
- [x] **Fase 1: Inisialisasi Proyek & Pintu Masuk (Telegram)**
  - [x] Buat bot Telegram baru via `@BotFather` dan simpan API Token.
  - [x] Inisialisasi repositori GitHub (`DeepArtha`) dengan struktur folder Python standar.
  - [x] Setup script Python dasar (`telebot` atau `python-telegram-bot`) untuk memastikan bot bisa merespons chat masuk.
  - [x] Setup *environment variables* (.env) untuk mengamankan seluruh API Key.

- [x] **Fase 2: Infrastruktur Database & Dashboard (Postgres & GSheet)**
  - [x] Rancang dan jalankan skema database PostgreSQL (Tabel: `pengeluaran`, `portofolio`, `kategori`).
  - [x] Pasang Qdrant untuk persiapan fitur RAG.
  - [x] Buat template Google Sheets murni untuk halaman ringkasan (*Executive Dashboard / Summary*).
  - [x] Konfigurasi **MCP (Model Context Protocol) Server** untuk Google Sheets agar bisa diakses oleh LLM.

- [ ] **Fase 3: Integrasi Data Eksternal & Eksekusi Kode (MCP & E2B)**
  - [ ] Hubungkan **MCP Yahoo Finance** ke dalam project untuk menarik data harga aset secara *real-time*.
  - [ ] Daftarkan API Key di [e2b.dev](https://e2b.dev).
  - [ ] Implementasikan modul `E2B Code Interpreter Sandbox` di Python untuk menjalankan script kalkulasi keuangan dan *plotting* grafik (`matplotlib`).
  - [ ] Uji coba membuat Agent menulis script Python, mengeksekusinya di E2B, dan mengirimkan file `.png` grafik kembali ke Telegram.

- [ ] **Fase 4: RAG Multimodal & Otak Agent (The Brain)**
  - [ ] Implementasikan modul **RAG Multimodal** (Vision LLM seperti Claude 3.5 Sonnet / GPT-4o) untuk membaca foto nota/kuitansi dari Telegram.
  - [ ] Buat fungsi ekstraksi otomatis: Mengubah gambar nota menjadi JSON terstruktur, lalu menyimpannya ke Postgres.
  - [ ] Bangun arsitektur **Deep Agent (Master Orchestrator)** dengan sistem *Plan-and-Execute* menggunakan LangChain/CrewAI/LangGraph.
  - [ ] Buat Sub-Agents terspesialisasi (Sub-Agent Pencatat, Sub-Agent Analis Pasar, Sub-Agent Pengingat).

- [ ] **Fase 5: Otomatisasi Sinkronisasi & Deployment**
  - [ ] Buat fungsi otomatisasi mingguan/bulanan (atau via *command* `/summary`) untuk memicu E2B melakukan agregasi data dari Postgres, lalu memperbarui dasbor Google Sheets via MCP.
  - [ ] Lakukan *testing* menyeluruh (end-to-end): Kirim nota ➡️ Cek Postgres ➡️ Minta `/summary` ➡️ Cek GSheet & Grafik Telegram.
  - [ ] Deploy aplikasi Python (Telegram Bot) ke platform cloud (Railway / Render / VPS) agar aktif 24/7.

-