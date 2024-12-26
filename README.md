# Run & Escape: The Infinite Maze Game

## 概要
`Run & Escape: The Infinite Maze Game` は、プレイヤーが敵から逃げるスリリングな体験を提供するゲームです。このゲームは、PythonとPygameを使って開発されており、AIを活用したコンテンツ生成機能を組み込んでいます。

プレイヤーは、迷路内で操作キャラクターを動かしながら敵から逃げ続け、できるだけ長く生き残ることを目指します。ゲームはエージェントの動きに A* アルゴリズムを活用し、知的な敵の行動をシミュレートします。

---

## 主な特徴
- **迷路生成**: ランダムな迷路を生成し、ゲームごとに異なるプレイ体験を提供。
- **A*アルゴリズム**: 敵キャラクターは最適な経路を探索し、プレイヤーを追い詰めます。
- **AIコンテンツ生成**: OpenAI APIを利用して、ゲームのイントロ、キャプション、メッセージを生成。
- **カスタム画像**: OpenAI DALL-E APIで生成されたカスタム画像をゲームに組み込み。
- **スリリングなゲームプレイ**: シンプルな操作で楽しめる緊張感ある体験を提供。

---

## 動作環境
以下の環境で動作確認されています：

- Python 3.8以上
- Pygame 2.1.2以上
- OpenAI Python SDK
- その他必要なライブラリ（`requirements.txt` を参照）

---

## インストール方法

1. リポジトリをクローンします。
   ```bash
   git clone https://github.com/R76H94/SIM.git
   cd SIM
   ```

2. 必要なライブラリをインストールします。
   ```bash
   pip install -r requirements.txt
   ```

3. OpenAI APIキーを環境変数として設定します。
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

---

## 実行方法
以下のコマンドでゲームを開始します。
```bash
python thief_vs_police_game_final.py
```

---

## ゲームのルール
1. ゲームを開始すると、イントロ画面が表示されます。
   - 画面右側にカスタム画像が表示されます。
   - テキストがスクロールし、ゲームの説明が表示されます。

2. カウントダウンが終了するとゲームが始まります。
   - プレイヤー（青色の四角）は迷路内で自由に移動可能。
   - 敵キャラクター（赤色の四角）がプレイヤーを追跡します。

3. プレイヤーは敵に捕まらないように逃げ続けます。

4. プレイヤーが捕まるとゲームオーバー。
   - ゲームオーバー画面で「Play Again」をクリックするとリスタートできます。

---

## 操作方法
- 矢印キーでプレイヤーを操作します。
  - 上矢印キー：上へ移動
  - 下矢印キー：下へ移動
  - 左矢印キー：左へ移動
  - 右矢印キー：右へ移動

---

## ファイル構成

```
.
├── thief_vs_police_game_final.py    # メインゲームスクリプト
├── requirements.txt      # 必要ライブラリのリスト
├── images/               # 生成された画像を保存するディレクトリ
├── README.md             # この説明書
├── thief_vs_police_game.py    # 初期のゲームスクリプト（使用しない）
```

---

## 使用されている技術
- **Python**: ゲームロジックの実装。
- **Pygame**: 2Dゲームの描画とインタラクション。
- **NumPy**: ランダム迷路生成。
- **OpenAI API**: テキスト生成と画像生成。
- **A*アルゴリズム**: 敵の経路探索。

---

## 注意事項
1. OpenAI APIキーは安全に管理してください。公開しないように注意してください。
2. 環境変数を利用してキーを管理することを推奨します。
3. 画像生成APIを利用するため、インターネット接続が必要です。

---

## 今後の課題
- スコア機能の追加
- 敵キャラクターのバリエーションを増加
- マルチプレイヤーモードの導入

---
