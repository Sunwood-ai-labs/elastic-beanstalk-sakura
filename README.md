<div align="center">

# 🚀 elastic-beanstalk-sakura

![d93075e45d922bf398b7557e402e737e8c79c743a1d034d1507bd89a](https://github.com/user-attachments/assets/8865069f-65e7-424e-bc60-841ecf1d370f)

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-FF4B4B.svg)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-✓-2496ED.svg)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-Elastic%20Beanstalk-FF9900.svg)](https://aws.amazon.com/elasticbeanstalk/)

[![GitHub](https://img.shields.io/github/license/Sunwood-ai-labs/elastic-beanstalk-sakura)](https://github.com/Sunwood-ai-labs/elastic-beanstalk-sakura)
[![GitHub issues](https://img.shields.io/github/issues/Sunwood-ai-labs/elastic-beanstalk-sakura)](https://github.com/Sunwood-ai-labs/elastic-beanstalk-sakura/issues)
[![GitHub stars](https://img.shields.io/github/stars/Sunwood-ai-labs/elastic-beanstalk-sakura)](https://github.com/Sunwood-ai-labs/elastic-beanstalk-sakura/stargazers)

</div>

## 📖 概要

AWS Elastic Beanstalk上でStreamlitアプリケーションを実行するためのDockerベースのプロジェクトです。

## 🛠️ 技術スタック

- **言語**: Python 3.9
- **フレームワーク**: Streamlit 1.28.0
- **データ処理**: Pandas 2.0.3, NumPy 1.25.2
- **コンテナ**: Docker
- **オーケストレーション**: Docker Compose
- **クラウド**: AWS Elastic Beanstalk

## 🏗️ プロジェクト構造

```plaintext
elastic-beanstalk-sakura/
├── .ebextensions/          # Elastic Beanstalk設定
├── .elasticbeanstalk/      # EB CLI設定
├── app.py                  # Streamlitアプリケーション
├── docker-compose.yml      # Docker Compose設定
├── Dockerfile              # Dockerイメージ定義
├── requirements.txt        # Python依存パッケージ
└── README.md               # プロジェクトドキュメント
```

## 🚦 実行方法

1. 依存パッケージのインストール
   ```bash
   pip install -r requirements.txt
   ```

2. Dockerイメージのビルド
   ```bash
   docker-compose build
   ```

3. コンテナの起動
   ```bash
   docker-compose up
   ```

4. アプリケーションへのアクセス
   - ブラウザで `http://localhost:8501` にアクセス

## 📊 機能

- ランダムデータの生成と表示
- データフレームの可視化
- 散布図の描画

## 📜 ライセンス

MIT License
