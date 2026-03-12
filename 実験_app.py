import streamlit as st
import pandas as pd
from collections import defaultdict

st.title("Club VES Talent OS")
def reverse_score(x):
    return 6-x


#pass
PASSWORD = "VES-nerve test"

def auth_gate():
    if "auth" not in st.session_state:
        st.session_state.auth = False

    if not st.session_state.auth:
        st.title("🔒 ICV Private Neuro System")
        st.caption("Authorized members only")

        pw = st.text_input("Access Key", type="password")

        if st.button("Enter"):
            if pw == PASSWORD:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Access Denied")

        st.stop()

auth_gate()

################################################
# 個人情報記録
################################################
st.header("PLYER INPUT")

name = st.text_input("名前")
age = st.number_input("年齢",)
height = st.number_input("身長",)
weihgt = st.number_input("体重",)

position = st.selectbox(
    "ポジション",
    ["GK","CB","SB","DMF","CMF","AMF","WG","CF"]
)
sub_position = st.selectbox(
        "サブポジション", 
        ["GK","CB","SB","DMF","CMF","AMF","WG","CF"]
        )
traninig_days = st.slider("週トレーニング回数",0,7)
match_days = st.slider("週試合数",0,10)

sleep  = st.slider("睡眠時間",1,10)

plyer_information = f'名前{name}\n年齢{age}歳\n身長{height}cm\n体重{weihgt}kg\n\
    ポジション{position}\n週トレーニング数{traninig_days}回\n週試合数{match_days}試合\n\
        睡眠時間{sleep}時間'

################################################
# タイプ定義
################################################

QUESTIONS = {

"神経タイプ診断":[
"試合中よく走り続ける",
"守備でチームを助けることが多い",
"体力で試合を支配するタイプ",
"プレッシングが得意",
"運動量で勝負する",

"周囲のスペースをよく見ている",
"パスコースを見つけるのが得意",
"試合の流れを読むのが得意",
"視野が広いと言われる",
"クリエイティブなプレーをする",

"チームの戦術理解が高い",
"ポジショニングを意識する",
"試合展開を考えて動く",
"守備ラインをコントロールする",
"戦術理解が強み",

"試合で感情がパフォーマンスを高める",
"勝負に強い",
"大事な試合で力を出す",
"ゴールに強い執念がある",
"チームを鼓舞する",

"瞬間的な判断が得意",
"反応速度が速い",
"カウンターが得意",
"ボール奪取の反応が速い",
"1vs1の反応が速い",

"ボールを受ける前に状況を見る",
"試合で予測して動く",
"相手の動きを読む",
"先回りするプレーが多い",
"判断スピードが速い"
],


"フィジカル診断":{

"スピード":[
"短距離スプリントが速い",
"加速が得意",
"カウンターで活躍する",
"スピードで相手を抜く",
"裏抜けが得意",
"30mダッシュが強み",
"スピード勝負が好き",
"スプリント回数が多い",
"相手より速いことが多い",
"スピードで守備できる"
],

"パワー":[
"フィジカルコンタクトが強い",
"空中戦が得意",
"体の強さが武器",
"相手に当たり負けない",
"ポストプレーが得意",
"強いシュートを打てる",
"デュエルに強い",
"ボールキープが得意",
"体格を活かせる",
"フィジカル勝負が得意"
],

"スタミナ":[
"試合最後まで走れる",
"運動量が多い",
"守備と攻撃を繰り返せる",
"長時間の試合でも落ちない",
"走行距離が多い",
"インターバルに強い",
"試合終盤でも走れる",
"長距離走が得意",
"試合中よく動く",
"運動量でチームに貢献する"
],

"アジリティ":[
"素早い方向転換",
"小さなスペースで動ける",
"フェイントが得意",
"細かいステップ",
"ドリブルで抜く",
"素早く体を動かせる",
"小回りが利く",
"瞬間ターン",
"1vs1突破",
"足さばきが速い"
],

"バランス":[
"ボール保持が安定",
"接触でも倒れない",
"体幹が強い",
"ポストプレー安定",
"ドリブル中安定",
"体勢が崩れにくい",
"バランス感覚良い",
"接触プレー安定",
"シュート体勢安定",
"キープ力"
]
},


"メンタル診断":{

"冷静":[
"プレッシャーでも冷静",
"ミスしても落ち着く",
"試合状況を冷静判断",
"焦らない",
"安定プレー"
],

"攻撃":[
"常にゴールを狙う",
"シュート意識高い",
"攻撃参加多い",
"リスクを取る",
"得点欲求"
],

"分析":[
"試合を分析する",
"映像を見る",
"戦術理解",
"相手研究",
"試合理解"
],

"闘争":[
"負けたくない気持ち強い",
"デュエルに強い",
"激しい守備",
"気持ちで戦う",
"試合で燃える"
],

"直感":[
"直感でプレーする",
"アイデア豊富",
"クリエイティブ",
"即興プレー",
"自由プレー"
]

}

}

#################################################
# N 神経診断
#################################################

st.header("N 神経タイプ診断")

N_sections = {
    "N1": "運動量神経",
    "N2": "守備神経",
    "N3": "判断神経",
    "N4": "空間認知神経",
    "N5": "闘争神経",
    "N6": "協調神経"
}

N_scores = {}

N_questions = QUESTIONS["神経タイプ診断"]

for i, section in enumerate(N_sections):

    st.subheader(N_sections[section])
    scores = []

    for j in range(5):

        q_index = i*5 + j
        question = N_questions[q_index]

        score = st.slider(
            question,
            1,
            5,
            key=f"N_{section}_{j}"
        )

        scores.append(score)

    N_scores[section] = sum(scores)
#################################################
# P 身体診断
#################################################

st.header("P 身体タイプ診断")

P_sections = {
    "P1": "スピード型",
    "P2": "持久型",
    "P3": "パワー型",
    "P4": "アジリティ型",
    "P5": "バランス型",
    "P6": "テクニック型"
}

P_scores = {}

for key, section in QUESTIONS["フィジカル診断"].items():

    st.subheader(key)
    scores = []

    for i, question in enumerate(section):

        score = st.slider(
            question,
            1,
            5,
            key=f"P_{key}_{i}"
        )

        scores.append(score)

    P_scores[key] = sum(scores)

#################################################
# M メンタル診断
#################################################

st.header("M メンタルタイプ診断")

M_sections = {
    "M1": "リーダー型",
    "M2": "冷静型",
    "M3": "努力型",
    "M4": "挑戦型",
    "M5": "安定型",
    "M6": "クリエイティブ型"
}

M_scores = {}

M_questions = QUESTIONS["メンタル診断"]

for key, section in QUESTIONS["メンタル診断"].items():

    st.subheader(key)
    scores = []

    for i, question in enumerate(section):

        score = st.slider(
            question,
            1,
            5,
            key=f"M_{key}_{i}"
        )

        scores.append(score)

    M_scores[key] = sum(scores)

#################################################
# タイプ決定
#################################################

N_type = max(N_scores, key=N_scores.get)
P_type = max(P_scores, key=P_scores.get)
M_type = max(M_scores, key=M_scores.get)

st.header("診断結果")

st.write("神経タイプ:", N_type)
st.write("身体タイプ:", P_type)
st.write("メンタルタイプ:", M_type)

player_type = f"{N_type}-{P_type}-{M_type}"

st.subheader("総合タイプ")
st.write(player_type)


# =========================================================
# CLUB VES DATA
# =========================================================

ABILITY_CATEGORIES = {
    "PHYSICAL": [
        "最大スピード","加速","減速能力","爆発力","最大筋力","相対筋力","下半身筋力","上半身筋力","体幹強度","筋持久力",
        "有酸素持久力","無酸素持久力","反復スプリント能力","敏捷性","方向転換速度","バランス","可動性","柔軟性","協調性","反応速度",
        "ジャンプ力","着地安定性","身体コントロール","怪我耐性","回復能力"
    ],
    "TECHNICAL": [
        "ボールコントロール","ファーストタッチ","プレッシャー下のタッチ","ドリブル","スピードドリブル","狭いスペースのドリブル",
        "ショートパス","ワンタッチパス","ロングパス","スルーパス","クロス","アーリークロス","シュート精度","シュートパワー","ボレー",
        "ミドルシュート","ヘディング","ボールキープ","ターン技術","1vs1攻撃","1vs1守備","タックル","インターセプト技術","セットプレーキック","セットプレー守備"
    ],
    "FOOTBALL_IQ": [
        "視野","スキャン能力","判断速度","判断精度","予測能力","空間認知","ポジショニング","タイミング","オフザボール動き","パターン認識",
        "戦術理解","試合分析能力","ゲームコントロール","創造性","リスク判断","相手分析","状況適応","プレッシャー下の判断","攻守切替判断","パスコース認知",
        "守備ライン理解","ビルドアップ理解","カウンター理解","試合テンポ理解","試合全体把握"
    ],
    "MENTAL": [
        "集中力","冷静さ","プレッシャー耐性","勝負強さ","モチベーション","自信","闘争心","レジリエンス","リーダーシップ","コミュニケーション",
        "チームワーク","自己管理","学習能力","規律性","継続力","責任感","プロ意識","目標意識","試合準備力","ミスからの回復",
        "ストレス管理","挑戦意欲","向上心","適応力","勝利意識"
    ],
}

MATCH_IQ_ABILITIES = [
    "視野","スキャン能力","判断速度","判断精度","予測能力","空間認知","ポジショニング","タイミング","オフザボール動き","パターン認識",
    "戦術理解","試合分析能力","ゲームコントロール","リスク判断","状況適応","プレッシャー下の判断","攻守切替判断","パスコース認知","守備ライン理解","試合テンポ理解"
]

# ユーザー提供DBをベースに厳選して保持
TRAINING_DB = {
    "PHYSICAL": [
        "10mスプリント","20mスプリント","30mスプリント","50mスプリント","10mフライングスプリント","20mフライングスプリント",
        "ボックスジャンプ","プライオメトリクスジャンプ","スクワット","デッドリフト","レジスタンススプリント","インターバルラン",
        "シャトルラン","ラダードリル","コーンドリル","片脚スクワット","プランク","サイドプランク","ジャンピングランジ","サイドステップドリル",
        "ヒップリフト","バーピー","ケトルベルスイング","メディシンボールスロー","アジリティラダー","ハードルドリル","ストレッチングルーチン",
        "ヒップアブダクション","レッグプレス","カーフレイズ","ダッシュ＆ターン","アジリティコーンドリル","ジャンプスクワット","メディシンボールスラム",
        "バランスボード","片脚ジャンプ","ローイングマシン","エアバイク","ケトルベルランジ","ハードルジャンプ","スプリント坂道","プッシュアップ",
        "チューブレジスタンス","負荷付きスプリント","ジャンピングプランク","メディシンボール投げ","スキップ＋ダッシュ","アジリティコーン＋反応",
        "坂道ラン＋スプリント","ジャンプ＋ダッシュ複合","短距離スプリント＋ターン","敏捷性＋方向転換","持久力インターバルラン","スピード持久走",
        "坂道インターバル","敏捷性＋スプリント","反応スプリントドリル","方向転換＋スプリント","加速＋減速ドリル","方向転換＋反応ドリル",
        "敏捷性＋フライングスプリント","スプリント＋シュート前ダッシュ"
    ],
    "TECHNICAL": [
        "リフティング","ボールタッチ","1vs1ドリブル","スラロームドリブル","ショートパス練習","ワンタッチパス練習","ロングパス練習",
        "スルーパス練習","クロス練習","アーリークロス","シュート精度","シュートパワー","ボレー練習","ミドルシュート","ヘディング練習",
        "ボールキープ練習","ターン技術練習","1vs1攻撃練習","1vs1守備練習","タックル練習","インターセプト練習","セットプレーキック","セットプレー守備",
        "ポゼッションゲーム","展開パス練習","ドリブル突破練習","クロスシュート","2vs2ボール回し","3vs3ショートパス","4vs4ラストパス練習",
        "シュート＋ターン練習","コーンターンドリブル","スピードドリブル","狭いスペースドリブル","ヘディングシュート","ワンタッチシュート",
        "スルーパス＋フィニッシュ","プレッシャードリブル","カットインドリブル","ボール保持ゲーム","2vs2守備練習","クロス＋ヘディング練習",
        "パス＋ムーブ練習","ターン＋シュート練習","ドリブル＋パス練習","1vs1突破練習","トラップ＋パス練習","狭いスペースワンタッチ",
        "パス回しスピード練習","クロス＋フィニッシュ練習","1vs1守備＋反応練習","2vs2＋判断速度強化","3vs3＋ポジショニング理解",
        "ボールキープ＋体幹複合","シュート＋プレス突破","スルーパス＋ドリブル連動","ワンタッチ＋オフザボール","パス＋ランニング＋ターン",
        "狭いスペース＋スピードドリブル","ドリブル＋シュート＋ターン","クロス＋判断速度ゲーム","1vs1攻撃＋反応速度","ポゼッション＋スペース認知",
        "ドリブル＋パス＋判断速度","クロス＋1vs1＋ヘディング","シュート＋ターン＋ランニング","ボールタッチ＋スピード＋判断",
        "ドリブル＋ポジショニング＋シュート","クロス＋シュート＋判断","ボール保持＋ドリブル＋判断","パス＋シュート＋オフザボール",
        "ドリブル＋判断速度＋ターン","クロス＋ヘディング＋シュート","1vs1＋シュート＋ドリブル"
    ],
    "FOOTBALL_IQ": [
        "視野練習","スキャン練習","制限タッチゲーム","ポジショナルゲーム","戦術理解ゲーム","映像分析","ゲーム分析","状況判断練習","パスコース認知",
        "守備ライン理解","ビルドアップ理解","カウンター理解","試合テンポ理解","オフザボール動き","パターン認識練習","判断速度ゲーム","判断精度練習",
        "予測能力練習","攻守切替判断練習","戦術シナリオ練習","プレッシャー下判断練習","ポジショニング修正練習","チームメイト動き予測","相手分析ゲーム",
        "スペース認知練習","試合全体把握練習","ボール保持判断練習","カウンター予測練習","戦術理解テスト","決定的瞬間判断練習","攻撃ルート判断",
        "守備ブロック理解","タイミング認識練習","ディフェンスラインコントロール","パスタイミングゲーム","オフザボール判断ゲーム","試合展開理解練習",
        "1vs1判断練習","2vs2戦術練習","3vs3戦術練習","ゲームテンポ調整練習","リスク判断練習","スペース制御練習","戦術動き理解","視野＋判断複合練習",
        "パス選択練習","攻守切替反応練習","チーム戦術理解","局面予測練習","守備位置理解","攻撃連動理解","パスタイミング判断"
    ],
    "MENTAL": [
        "集中ドリル","プレッシャーゲーム","デュエルゲーム","チームゲーム","メンタルトレーニング","自己管理練習","目標設定練習","ミス回復練習",
        "ストレス管理練習","挑戦意欲強化","勝利意識強化","向上心養成","闘争心練習","モチベーション強化","冷静さ養成","リーダーシップ練習","チームワーク向上",
        "自信強化","集中力持続練習","心理プレッシャー克服","意思決定メンタル練習","状況適応練習","メンタル耐性強化","継続力養成","責任感強化",
        "プロ意識向上","自己反省練習","習慣化練習","試合準備力強化","目標達成意識練習","ポジティブ思考練習","プレッシャー耐性ゲーム","勝負強化シナリオ",
        "レジリエンス練習","心理トラブルシュート","挑戦的タスク練習","感情コントロール練習","集中維持ゲーム","競争意識強化","モチベーション維持練習",
        "判断力メンタル強化","チーム連携メンタル練習","冷静判断ゲーム","自己信頼向上練習","メンタルフィードバック練習","意志力強化練習","勝利意識シナリオ",
        "継続トレーニング","プレッシャー下判断練習","試合メンタルシナリオ","集中力＋スプリント練習","反応力＋プレッシャー練習","闘争心＋判断力練習",
        "チーム連携＋意思決定練習","メンタル耐性＋体幹練習"
    ]
}

ABILITY_TO_DOMAIN = {
    # PHYSICAL
    "最大スピード":"PHYSICAL","加速":"PHYSICAL","減速能力":"PHYSICAL","爆発力":"PHYSICAL","最大筋力":"PHYSICAL","相対筋力":"PHYSICAL",
    "下半身筋力":"PHYSICAL","上半身筋力":"PHYSICAL","体幹強度":"PHYSICAL","筋持久力":"PHYSICAL","有酸素持久力":"PHYSICAL","無酸素持久力":"PHYSICAL",
    "反復スプリント能力":"PHYSICAL","敏捷性":"PHYSICAL","方向転換速度":"PHYSICAL","バランス":"PHYSICAL","可動性":"PHYSICAL","柔軟性":"PHYSICAL",
    "協調性":"PHYSICAL","反応速度":"PHYSICAL","ジャンプ力":"PHYSICAL","着地安定性":"PHYSICAL","身体コントロール":"PHYSICAL","怪我耐性":"PHYSICAL","回復能力":"PHYSICAL",
    # TECHNICAL
    "ボールコントロール":"TECHNICAL","ファーストタッチ":"TECHNICAL","プレッシャー下のタッチ":"TECHNICAL","ドリブル":"TECHNICAL","スピードドリブル":"TECHNICAL",
    "狭いスペースのドリブル":"TECHNICAL","ショートパス":"TECHNICAL","ワンタッチパス":"TECHNICAL","ロングパス":"TECHNICAL","スルーパス":"TECHNICAL",
    "クロス":"TECHNICAL","アーリークロス":"TECHNICAL","シュート精度":"TECHNICAL","シュートパワー":"TECHNICAL","ボレー":"TECHNICAL","ミドルシュート":"TECHNICAL",
    "ヘディング":"TECHNICAL","ボールキープ":"TECHNICAL","ターン技術":"TECHNICAL","1vs1攻撃":"TECHNICAL","1vs1守備":"TECHNICAL","タックル":"TECHNICAL",
    "インターセプト技術":"TECHNICAL","セットプレーキック":"TECHNICAL","セットプレー守備":"TECHNICAL",
    # IQ
    "視野":"FOOTBALL_IQ","スキャン能力":"FOOTBALL_IQ","判断速度":"FOOTBALL_IQ","判断精度":"FOOTBALL_IQ","予測能力":"FOOTBALL_IQ","空間認知":"FOOTBALL_IQ",
    "ポジショニング":"FOOTBALL_IQ","タイミング":"FOOTBALL_IQ","オフザボール動き":"FOOTBALL_IQ","パターン認識":"FOOTBALL_IQ","戦術理解":"FOOTBALL_IQ",
    "試合分析能力":"FOOTBALL_IQ","ゲームコントロール":"FOOTBALL_IQ","創造性":"FOOTBALL_IQ","リスク判断":"FOOTBALL_IQ","相手分析":"FOOTBALL_IQ",
    "状況適応":"FOOTBALL_IQ","プレッシャー下の判断":"FOOTBALL_IQ","攻守切替判断":"FOOTBALL_IQ","パスコース認知":"FOOTBALL_IQ","守備ライン理解":"FOOTBALL_IQ",
    "ビルドアップ理解":"FOOTBALL_IQ","カウンター理解":"FOOTBALL_IQ","試合テンポ理解":"FOOTBALL_IQ","試合全体把握":"FOOTBALL_IQ",
    # MENTAL
    "集中力":"MENTAL","冷静さ":"MENTAL","プレッシャー耐性":"MENTAL","勝負強さ":"MENTAL","モチベーション":"MENTAL","自信":"MENTAL","闘争心":"MENTAL",
    "レジリエンス":"MENTAL","リーダーシップ":"MENTAL","コミュニケーション":"MENTAL","チームワーク":"MENTAL","自己管理":"MENTAL","学習能力":"MENTAL",
    "規律性":"MENTAL","継続力":"MENTAL","責任感":"MENTAL","プロ意識":"MENTAL","目標意識":"MENTAL","試合準備力":"MENTAL","ミスからの回復":"MENTAL",
    "ストレス管理":"MENTAL","挑戦意欲":"MENTAL","向上心":"MENTAL","適応力":"MENTAL","勝利意識":"MENTAL"
}

ABILITY_TO_TRAININGS = {
    "最大スピード":["10mスプリント","20mスプリント","30mスプリント","10mフライングスプリント","20mフライングスプリント","スプリント坂道"],
    "加速":["レジスタンススプリント","加速＋減速ドリル","ダッシュ＆ターン","10mスプリント"],
    "減速能力":["加速＋減速ドリル","方向転換＋スプリント","方向転換＋反応ドリル","ラダードリル"],
    "爆発力":["ボックスジャンプ","プライオメトリクスジャンプ","ジャンプスクワット","ジャンプ＋ダッシュ複合"],
    "最大筋力":["スクワット","デッドリフト","レッグプレス","ケトルベルスイング"],
    "相対筋力":["片脚スクワット","ケトルベルランジ","ジャンピングランジ","片脚ランジジャンプ"],
    "下半身筋力":["スクワット","ジャンプスクワット","レッグプレス","ケトルベルランジ"],
    "上半身筋力":["プッシュアップ","チューブレジスタンス","バトルロープ","メディシンボールスラム"],
    "体幹強度":["プランク","サイドプランク","ヒップリフト","バランスボード","メンタル耐性＋体幹練習"],
    "筋持久力":["インターバルラン","シャトルラン","持久力インターバルラン","バーピー"],
    "有酸素持久力":["インターバルラン","エアバイク","ローイングマシン","スピード持久走"],
    "無酸素持久力":["シャトルラン","スピード持久走","坂道インターバル","短距離スプリント＋ターン"],
    "反復スプリント能力":["シャトルラン","スプリント坂道","短距離スプリント＋ターン","坂道ラン＋スプリント"],
    "敏捷性":["ラダードリル","コーンドリル","アジリティラダー","敏捷性＋方向転換","アジリティコーン＋反応"],
    "方向転換速度":["方向転換＋スプリント","ラダードリル","コーンドリル","敏捷性＋方向転換"],
    "バランス":["バランスボード","片脚スクワット","片脚バランス＋ジャンプ","片脚ジャンプ＋バランス"],
    "可動性":["ストレッチングルーチン","ヒップアブダクション","カーフレイズ"],
    "柔軟性":["ストレッチングルーチン","ヒップアブダクション"],
    "協調性":["ラダードリル","ボールタッチ","アジリティラダー"],
    "反応速度":["反応スプリントドリル","アジリティコーン＋反応","方向転換＋反応ドリル"],
    "ジャンプ力":["ボックスジャンプ","ジャンプスクワット","ハードルジャンプ"],
    "着地安定性":["片脚ジャンプ","バランスボード","片脚バランス＋ジャンプ"],
    "身体コントロール":["片脚スクワット","バランスボード","プランク","片脚ジャンプ＋バランス"],
    "怪我耐性":["ストレッチングルーチン","プランク","ヒップアブダクション","バランスボード"],
    "回復能力":["エアバイク","ローイングマシン","ストレッチングルーチン"],

    "ボールコントロール":["ボールタッチ","リフティング","トラップ＋パス練習"],
    "ファーストタッチ":["トラップ＋パス練習","ボールタッチ","狭いスペースワンタッチ"],
    "プレッシャー下のタッチ":["プレッシャードリブル","狭いスペースワンタッチ","ポゼッションゲーム"],
    "ドリブル":["1vs1ドリブル","スラロームドリブル","ドリブル突破練習"],
    "スピードドリブル":["スピードドリブル","狭いスペース＋スピードドリブル","ターン＋スピードドリブル"],
    "狭いスペースのドリブル":["狭いスペースドリブル","コーンターンドリブル","プレッシャードリブル"],
    "ショートパス":["ショートパス練習","3vs3ショートパス","パス＋ムーブ練習"],
    "ワンタッチパス":["ワンタッチパス練習","狭いスペースワンタッチ","ワンタッチ＋オフザボール"],
    "ロングパス":["ロングパス練習","展開パス練習","パス＋ランニング＋ターン"],
    "スルーパス":["スルーパス練習","スルーパス＋フィニッシュ","スルーパス＋ドリブル連動"],
    "クロス":["クロス練習","クロス＋フィニッシュ練習","クロス＋シュート＋判断"],
    "アーリークロス":["アーリークロス","クロス練習","クロス＋フィニッシュ練習"],
    "シュート精度":["シュート精度","ワンタッチシュート","シュート＋ターン練習"],
    "シュートパワー":["シュートパワー","ミドルシュート","シュート＋ジャンプ練習"],
    "ボレー":["ボレー練習","ワンタッチシュート","クロス＋ヘディング＋シュート"],
    "ミドルシュート":["ミドルシュート","シュートパワー","シュート＋ターン＋ランニング"],
    "ヘディング":["ヘディング練習","ヘディングシュート","クロス＋ヘディング練習"],
    "ボールキープ":["ボールキープ練習","ボール保持ゲーム","ボールキープ＋体幹複合"],
    "ターン技術":["ターン技術練習","コーンターンドリブル","ターン＋シュート練習"],
    "1vs1攻撃":["1vs1攻撃練習","1vs1突破練習","1vs1＋シュート＋ドリブル"],
    "1vs1守備":["1vs1守備練習","1vs1守備＋反応練習","2vs2守備練習"],
    "タックル":["タックル練習","2vs2守備練習","1vs1守備練習"],
    "インターセプト技術":["インターセプト練習","2vs2守備練習","ヘディング＋ディフェンス"],
    "セットプレーキック":["セットプレーキック","クロス練習","ロングパス練習"],
    "セットプレー守備":["セットプレー守備","ヘディング＋ディフェンス","2vs2守備練習"],

    "視野":["視野練習","スキャン練習","視野＋判断複合練習"],
    "スキャン能力":["スキャン練習","視野練習","スペース認知練習"],
    "判断速度":["判断速度ゲーム","制限タッチゲーム","決定的瞬間判断練習"],
    "判断精度":["判断精度練習","プレッシャー下判断練習","パス選択練習"],
    "予測能力":["予測能力練習","局面予測練習","カウンター予測練習"],
    "空間認知":["スペース認知練習","視野練習","ポジショナルゲーム"],
    "ポジショニング":["ポジショニング修正練習","守備位置理解","オフザボール判断ゲーム"],
    "タイミング":["タイミング認識練習","パスタイミングゲーム","パスタイミング判断"],
    "オフザボール動き":["オフザボール動き","オフザボール判断ゲーム","攻撃連動理解"],
    "パターン認識":["パターン認識練習","局面予測練習","ゲーム分析"],
    "戦術理解":["戦術理解ゲーム","戦術理解テスト","戦術動き理解"],
    "試合分析能力":["映像分析","ゲーム分析","相手分析ゲーム"],
    "ゲームコントロール":["ポジショナルゲーム","ゲームテンポ調整練習","試合テンポ理解"],
    "創造性":["視野＋判断複合練習","パス選択練習","攻撃ルート判断"],
    "リスク判断":["リスク判断練習","プレッシャー下判断練習","ボール保持判断練習"],
    "相手分析":["相手分析ゲーム","映像分析","ゲーム分析"],
    "状況適応":["状況判断練習","試合展開理解練習","オフザボール判断ゲーム"],
    "プレッシャー下の判断":["プレッシャー下判断練習","判断速度ゲーム","制限タッチゲーム"],
    "攻守切替判断":["攻守切替判断練習","攻守切替反応練習","カウンター理解"],
    "パスコース認知":["パスコース認知","パス選択練習","ビルドアップ理解"],
    "守備ライン理解":["守備ライン理解","ディフェンスラインコントロール","守備ブロック理解"],
    "ビルドアップ理解":["ビルドアップ理解","チーム戦術理解","ポジショナルゲーム"],
    "カウンター理解":["カウンター理解","カウンター予測練習","攻守切替判断練習"],
    "試合テンポ理解":["試合テンポ理解","ゲームテンポ調整練習","試合全体把握練習"],
    "試合全体把握":["試合全体把握練習","ゲーム分析","試合展開理解練習"],

    "集中力":["集中ドリル","集中力持続練習","集中維持ゲーム"],
    "冷静さ":["冷静さ養成","冷静判断ゲーム","感情コントロール練習"],
    "プレッシャー耐性":["プレッシャーゲーム","プレッシャー耐性ゲーム","心理プレッシャー克服"],
    "勝負強さ":["勝負強化シナリオ","勝利意識シナリオ","試合メンタルシナリオ"],
    "モチベーション":["モチベーション強化","モチベーション維持練習","挑戦意欲強化"],
    "自信":["自信強化","自己信頼向上練習","ポジティブ思考練習"],
    "闘争心":["デュエルゲーム","闘争心練習","競争意識強化"],
    "レジリエンス":["レジリエンス練習","ミス回復練習","心理トラブルシュート"],
    "リーダーシップ":["リーダーシップ練習","チームゲーム","チーム連携＋意思決定練習"],
    "コミュニケーション":["チームゲーム","チームワーク向上","チーム連携メンタル練習"],
    "チームワーク":["チームゲーム","チームワーク向上","チーム連携＋意思決定練習"],
    "自己管理":["自己管理練習","習慣化練習","プロ意識向上"],
    "学習能力":["自己反省練習","メンタルフィードバック練習","映像分析"],
    "規律性":["習慣化練習","自己管理練習","プロ意識向上"],
    "継続力":["継続力養成","継続トレーニング","目標設定練習"],
    "責任感":["責任感強化","自己管理練習","試合準備力強化"],
    "プロ意識":["プロ意識向上","自己管理練習","習慣化練習"],
    "目標意識":["目標設定練習","目標達成意識練習","モチベーション強化"],
    "試合準備力":["試合準備力強化","試合メンタルシナリオ","自己管理練習"],
    "ミスからの回復":["ミス回復練習","レジリエンス練習","自己信頼向上練習"],
    "ストレス管理":["ストレス管理練習","感情コントロール練習","心理トラブルシュート"],
    "挑戦意欲":["挑戦意欲強化","挑戦的タスク練習","モチベーション強化"],
    "向上心":["向上心養成","目標達成意識練習","継続トレーニング"],
    "適応力":["状況適応練習","意思決定メンタル練習","試合メンタルシナリオ"],
    "勝利意識":["勝利意識強化","勝利意識シナリオ","闘争心練習"]
}

POSITION_WEIGHTS = {
    "WG": {"最大スピード":5,"加速":5,"反復スプリント能力":4,"敏捷性":4,"方向転換速度":4,"ドリブル":5,"スピードドリブル":5,"狭いスペースのドリブル":4,"1vs1攻撃":5,"クロス":4,"アーリークロス":4,"シュート精度":3,"視野":3,"スキャン能力":3,"判断速度":4,"オフザボール動き":5,"空間認知":4,"闘争心":3,"自信":3,"勝利意識":3},
    "ST": {"最大スピード":4,"加速":5,"ジャンプ力":4,"シュート精度":5,"シュートパワー":5,"ボレー":4,"ミドルシュート":4,"ヘディング":4,"1vs1攻撃":4,"ボールキープ":4,"オフザボール動き":5,"タイミング":5,"予測能力":4,"勝負強さ":5,"自信":4},
    "AMF": {"敏捷性":3,"方向転換速度":3,"ボールコントロール":5,"ファーストタッチ":5,"ショートパス":5,"ワンタッチパス":5,"スルーパス":5,"ロングパス":4,"ドリブル":4,"視野":5,"スキャン能力":5,"判断速度":4,"判断精度":5,"空間認知":5,"創造性":5,"ゲームコントロール":5,"冷静さ":4,"自信":4,"集中力":4},
    "CM": {"筋持久力":4,"有酸素持久力":5,"反復スプリント能力":4,"ボールコントロール":4,"ショートパス":5,"ワンタッチパス":5,"ロングパス":4,"視野":5,"スキャン能力":5,"判断速度":4,"判断精度":5,"空間認知":5,"試合テンポ理解":5,"集中力":4,"責任感":4,"チームワーク":5},
    "DM": {"最大筋力":4,"体幹強度":4,"敏捷性":3,"ショートパス":4,"ロングパス":4,"ボールキープ":4,"ポジショニング":5,"守備ライン理解":5,"パスコース認知":5,"予測能力":5,"攻守切替判断":5,"冷静さ":5,"集中力":5,"責任感":5},
    "SB": {"最大スピード":5,"加速":5,"反復スプリント能力":5,"敏捷性":4,"クロス":4,"ショートパス":4,"ドリブル":4,"1vs1守備":4,"オフザボール動き":5,"攻守切替判断":5,"空間認知":4,"闘争心":4,"集中力":4},
    "CB": {"最大筋力":5,"下半身筋力":5,"ジャンプ力":5,"バランス":4,"ヘディング":5,"1vs1守備":5,"タックル":5,"インターセプト技術":5,"ポジショニング":5,"守備ライン理解":5,"予測能力":5,"パスコース認知":4,"闘争心":5,"責任感":5,"集中力":5},
    "GK": {"反応速度":5,"ジャンプ力":5,"バランス":5,"身体コントロール":5,"判断速度":4,"予測能力":5,"ポジショニング":5,"冷静さ":5,"集中力":5,"責任感":5},
}

N_BONUS = {
    "N1 運動駆動型": {"反復スプリント能力":1.08,"筋持久力":1.08,"有酸素持久力":1.08,"攻守切替判断":1.08},
    "N2 知覚型": {"視野":1.08,"スキャン能力":1.08,"空間認知":1.08,"判断精度":1.08},
    "N3 戦術型": {"戦術理解":1.08,"ポジショニング":1.08,"試合テンポ理解":1.08,"守備ライン理解":1.08},
    "N4 衝動型": {"1vs1攻撃":1.08,"シュート精度":1.08,"シュートパワー":1.08,"勝負強さ":1.08},
    "N5 反応型": {"反応速度":1.08,"判断速度":1.08,"1vs1守備":1.08,"攻守切替判断":1.08},
    "N6 予測型": {"予測能力":1.08,"パスコース認知":1.08,"インターセプト技術":1.08,"ポジショニング":1.08},
}
P_BONUS = {
    "P1 スピード": {"最大スピード":1.08,"加速":1.08,"反復スプリント能力":1.08},
    "P2 パワー": {"最大筋力":1.08,"下半身筋力":1.08,"上半身筋力":1.08,"ボールキープ":1.08},
    "P3 スタミナ": {"有酸素持久力":1.08,"筋持久力":1.08,"無酸素持久力":1.08},
    "P4 アジリティ": {"敏捷性":1.08,"方向転換速度":1.08,"狭いスペースのドリブル":1.08,"ターン技術":1.08},
    "P5 バランス": {"バランス":1.08,"身体コントロール":1.08,"着地安定性":1.08,"体幹強度":1.08},
}
M_BONUS = {
    "M1 冷静": {"冷静さ":1.08,"プレッシャー耐性":1.08,"判断精度":1.08,"ミスからの回復":1.08},
    "M2 攻撃": {"シュート精度":1.08,"オフザボール動き":1.08,"勝利意識":1.08,"勝負強さ":1.08},
    "M3 分析": {"試合分析能力":1.08,"戦術理解":1.08,"相手分析":1.08,"学習能力":1.08},
    "M4 闘争": {"闘争心":1.08,"1vs1守備":1.08,"タックル":1.08,"勝負強さ":1.08},
    "M5 直感": {"創造性":1.08,"1vs1攻撃":1.08,"スルーパス":1.08,"状況適応":1.08},
}

PHV_OPTIONS = ["PHV前","PHV中","PHV後"]
AGE_STAGE_OPTIONS = ["U8-U10","U11-U12","U13-U15","U16-U18","18+"]

AGE_DOMAIN_COEFFICIENTS = {
    "U8-U10": {"PHYSICAL":0.95,"TECHNICAL":1.20,"FOOTBALL_IQ":1.05,"MENTAL":1.00},
    "U11-U12": {"PHYSICAL":1.00,"TECHNICAL":1.20,"FOOTBALL_IQ":1.10,"MENTAL":1.00},
    "U13-U15": {"PHYSICAL":1.05,"TECHNICAL":1.10,"FOOTBALL_IQ":1.15,"MENTAL":1.05},
    "U16-U18": {"PHYSICAL":1.10,"TECHNICAL":1.05,"FOOTBALL_IQ":1.10,"MENTAL":1.05},
    "18+": {"PHYSICAL":1.05,"TECHNICAL":1.00,"FOOTBALL_IQ":1.10,"MENTAL":1.10},
}
PHV_DOMAIN_COEFFICIENTS = {
    "PHV前": {"PHYSICAL":0.95,"TECHNICAL":1.15,"FOOTBALL_IQ":1.05,"MENTAL":1.00},
    "PHV中": {"PHYSICAL":1.00,"TECHNICAL":1.05,"FOOTBALL_IQ":1.05,"MENTAL":1.00},
    "PHV後": {"PHYSICAL":1.12,"TECHNICAL":1.00,"FOOTBALL_IQ":1.05,"MENTAL":1.00},
}

MATCH_METRIC_TO_ABILITIES = {
    "ドリブル成功率": ["ドリブル","スピードドリブル","狭いスペースのドリブル","1vs1攻撃"],
    "パス成功率": ["ショートパス","ワンタッチパス","ロングパス","判断精度"],
    "デュエル勝率": ["1vs1守備","タックル","体幹強度","下半身筋力"],
    "スプリント数": ["有酸素持久力","反復スプリント能力","最大スピード"],
    "被突破数": ["1vs1守備","判断速度","ポジショニング","守備ライン理解"],
}



################### chat GPT ##################

#######必要関数
def get_height_weight_coeff(position: str, height: int, weight: int) -> float:
    coeff = 1.0
    # 簡易補正
    if position in ["CB", "GK", "ST"]:
        if height >= 182:
            coeff *= 1.05
        elif height <= 168:
            coeff *= 0.98
    elif position in ["WG", "SB", "AMF"]:
        if height <= 172:
            coeff *= 1.03
        elif height >= 185:
            coeff *= 0.98

    if position in ["WG", "SB", "AMF"]:
        if weight <= 65:
            coeff *= 1.03
        elif weight >= 78:
            coeff *= 0.98
    elif position in ["CB", "DM", "ST"]:
        if weight >= 75:
            coeff *= 1.03
        elif weight <= 60:
            coeff *= 0.98
    return coeff
def get_age_domain_coeff(domain: str, age_stage: str) -> float:
    return AGE_DOMAIN_COEFFICIENTS[age_stage][domain]
def get_phv_domain_coeff(domain: str, phv_stage: str) -> float:
    return PHV_DOMAIN_COEFFICIENTS[phv_stage][domain]
def get_type_bonus(ability: str, n_type: str, p_type: str, m_type: str) -> float:
    bonus = 1.0
    bonus *= N_BONUS.get(n_type, {}).get(ability, 1.0)
    bonus *= P_BONUS.get(p_type, {}).get(ability, 1.0)
    bonus *= M_BONUS.get(m_type, {}).get(ability, 1.0)
    return bonus
def weakness_degree(score: int) -> int:
    return {1: 5, 2: 4, 3: 2, 4: 1, 5: 0}[score]



def infer_age_stage(age: int) -> str:
    if age <= 10:
        return "U8-U10"
    if age <= 12:
        return "U11-U12"
    if age <= 15:
        return "U13-U15"
    if age <= 18:
        return "U16-U18"
    return "18+"
def calc_category_averages(scores: dict) -> dict:
    out = {}
    for category, abilities in ABILITY_CATEGORIES.items():
        vals = [scores[a] for a in abilities]
        out[category] = round(sum(vals) / len(vals), 2)
    return out

def calc_match_iq(scores: dict) -> float:
    total = sum(scores[a] for a in MATCH_IQ_ABILITIES)
    max_total = len(MATCH_IQ_ABILITIES) * 5
    return round((total / max_total) * 100, 1)

def calc_position_fit(scores: dict, position: str, height: int, weight: int, phv_stage: str, experience_bonus: float = 0.0, match_bonus: float = 0.0) -> float:
    weights = POSITION_WEIGHTS[position]
    weighted_sum = 0
    weight_total = 0
    for ability, weight in weights.items():
        weighted_sum += scores.get(ability, 3) * weight
        weight_total += weight
    base = (weighted_sum / (weight_total * 5)) * 100
    body_coeff = get_height_weight_coeff(position, height, weight)
    phv_coeff = 1.02 if phv_stage == "PHV後" else 1.0
    final = base * body_coeff * phv_coeff + experience_bonus + match_bonus
    return round(final, 1)
def calc_match_index(match_metrics: dict) -> float:
    parts = []
    for key, val in match_metrics.items():
        if key == "被突破数":
            # 少ないほどよい。0〜10を仮定
            mapped = max(0, min(100, 100 - val * 10))
        else:
            mapped = val
        parts.append(mapped)
    if not parts:
        return 60.0
    return round(sum(parts) / len(parts), 1)
def calc_growth_projection(scores: dict, age_stage: str, phv_stage: str, n_type: str, p_type: str, m_type: str) -> pd.DataFrame:
    rows = []
    for ability, score in scores.items():
        domain = ABILITY_TO_DOMAIN[ability]
        base_coeff = {1:0.8, 2:1.0, 3:1.2, 4:1.0, 5:0.4}[score]
        age_coeff = get_age_domain_coeff(domain, age_stage)
        phv_coeff = get_phv_domain_coeff(domain, phv_stage)
        type_coeff = get_type_bonus(ability, n_type, p_type, m_type)
        growth_score = base_coeff * age_coeff * phv_coeff * type_coeff
        rows.append({"能力": ability, "成長予測スコア": round(growth_score, 3)})
    df = pd.DataFrame(rows).sort_values("成長予測スコア", ascending=False)
    return df
def calc_training_priorities(scores: dict, position: str, age_stage: str, phv_stage: str,
                             n_type: str, p_type: str, m_type: str, match_metrics: dict,
                             goal_focus: list[str]) -> pd.DataFrame:
    match_bonus_map = defaultdict(lambda: 1.0)

    for metric, low_related_abilities in MATCH_METRIC_TO_ABILITIES.items():
        val = match_metrics.get(metric)
        if val is None:
            continue
        if metric == "被突破数":
            if val >= 4:
                for ab in low_related_abilities:
                    match_bonus_map[ab] = 1.08
        else:
            if val <= 55:
                for ab in low_related_abilities:
                    match_bonus_map[ab] = 1.08

    goal_bonus_map = defaultdict(lambda: 1.0)
    for focus in goal_focus:
        for ability, trainings in ABILITY_TO_TRAININGS.items():
            if focus and any(focus in t for t in trainings):
                goal_bonus_map[ability] = 1.06

    rows = []
    weights = POSITION_WEIGHTS.get(position, {})
    for ability, score in scores.items():
        domain = ABILITY_TO_DOMAIN[ability]
        priority = (
            weakness_degree(score)
            * weights.get(ability, 1)
            * get_age_domain_coeff(domain, age_stage)
            * get_phv_domain_coeff(domain, phv_stage)
            * get_type_bonus(ability, n_type, p_type, m_type)
            * match_bonus_map[ability]
            * goal_bonus_map[ability]
        )
        rows.append({
            "能力": ability,
            "スコア": score,
            "優先度": round(priority, 2),
            "カテゴリ": domain
        })
    df = pd.DataFrame(rows).sort_values("優先度", ascending=False)
    return df
def select_trainings_from_priorities(priority_df: pd.DataFrame, top_n_abilities: int = 5) -> pd.DataFrame:
    selected = []
    seen = set()
    top_df = priority_df.head(top_n_abilities)

    for _, row in top_df.iterrows():
        ability = row["能力"]
        domain = ABILITY_TO_DOMAIN[ability]
        trainings = ABILITY_TO_TRAININGS.get(ability, [])[:3]
        for idx, t in enumerate(trainings):
            if t not in seen:
                selected.append({
                    "能力": ability,
                    "トレーニング": t,
                    "カテゴリ": domain,
                    "タイプ": "基礎" if idx == 0 else "応用" if idx == 1 else "複合"
                })
                seen.add(t)
    return pd.DataFrame(selected)
def generate_weekly_plan(training_df: pd.DataFrame) -> dict:
    by_cat = defaultdict(list)
    for _, row in training_df.iterrows():
        by_cat[row["カテゴリ"]].append(row["トレーニング"])

    plan = {
        "月": [],
        "火": [],
        "水": [],
        "木": [],
        "金": [],
        "土": ["試合 / ゲーム形式"],
        "日": ["回復 / モビリティ / 振り返り"]
    }

    plan["月"] = by_cat["PHYSICAL"][:2] + by_cat["TECHNICAL"][:1]
    plan["火"] = by_cat["TECHNICAL"][1:3] + by_cat["FOOTBALL_IQ"][:1]
    plan["水"] = by_cat["FOOTBALL_IQ"][1:3] + by_cat["MENTAL"][:1]
    plan["木"] = by_cat["PHYSICAL"][2:4] + by_cat["TECHNICAL"][3:4]
    plan["金"] = by_cat["MENTAL"][1:3] + by_cat["FOOTBALL_IQ"][3:4]

    for day in ["月", "火", "水", "木", "金"]:
        if not plan[day]:
            plan[day] = ["個別メニュー調整"]
    return plan
def top_strengths_and_weaknesses(scores: dict):
    s_df = pd.DataFrame([{"能力": k, "スコア": v} for k, v in scores.items()])
    strengths = s_df.sort_values(["スコア", "能力"], ascending=[False, True]).head(5)
    weaknesses = s_df.sort_values(["スコア", "能力"], ascending=[True, True]).head(5)
    return strengths, weaknesses
def calc_player_rating(scores: dict, n_type: str, p_type: str, m_type: str, age_stage: str, phv_stage: str,
                       height: int, weight: int, match_index: float) -> float:
    ability_index = (sum(scores.values()) / (len(scores) * 5)) * 100

    # タイプ適合の簡易平均
    favored = []
    for src in [N_BONUS.get(n_type, {}), P_BONUS.get(p_type, {}), M_BONUS.get(m_type, {})]:
        favored.extend(list(src.keys()))
    if favored:
        type_fit_raw = sum(scores.get(a, 3) for a in favored) / (len(favored) * 5) * 100
    else:
        type_fit_raw = 60.0
    type_index = 0.95 + (type_fit_raw / 100) * 0.10  # 0.95〜1.05

    body_index = ((get_age_domain_coeff("PHYSICAL", age_stage) + get_phv_domain_coeff("PHYSICAL", phv_stage)) / 2)
    body_index *= get_height_weight_coeff("CB", height, weight) * 0.5 + 0.5  # 補正を弱くする

    match_coeff = 0.90 + (match_index / 100) * 0.20  # 0.90〜1.10
    rating = ability_index * type_index * body_index * match_coeff
    return round(rating, 1)
def relation_analysis(scores: dict) -> list[str]:
    notes = []
    if scores["最大スピード"] >= 4 and scores["加速"] <= 2:
        notes.append("トップスピードは高いが、出足の加速に課題がある。")
    if scores["視野"] >= 4 and scores["判断速度"] <= 2:
        notes.append("状況は見えているが、プレー選択の処理速度に課題がある。")
    if scores["闘争心"] >= 4 and scores["冷静さ"] <= 2:
        notes.append("勝負への強さはあるが、感情コントロールに課題がある。")
    if scores["ドリブル"] >= 4 and scores["判断精度"] <= 2:
        notes.append("個で剥がす力は高いが、次の選択の精度向上が必要。")
    if scores["1vs1守備"] >= 4 and scores["守備ライン理解"] <= 2:
        notes.append("個の守備対応は強いが、組織守備理解に改善余地がある。")
    return notes if notes else ["大きな関係性アラートはなし。総合的にバランスを見ながら育成する。"]



##############プラスUI

# =========================================================
# UI
# =========================================================

st.title("CLUB VES AI DEVELOPMENT PLATFORM")
st.caption("100能力評価 × 150タイプ × 係数補正 × AIトレーニング生成")

with st.sidebar:
    st.header("PLAYER INPUT")
    player_name = name
    age = age
    age_stage = infer_age_stage(age)
    height = height
    weight = weihgt
    position = position
    phv_stage = st.selectbox("PHV段階", PHV_OPTIONS, index=1)
    n_type = st.selectbox("神経タイプ", N_type)
    p_type = st.selectbox("フィジカルタイプ", P_type)
    m_type = st.selectbox("メンタルタイプ", M_type)

    st.divider()
    st.subheader("試合データ")
    match_metrics = {
        "パス成功率": st.slider("パス成功率", 0, 100, 70),
        "ドリブル成功率": st.slider("ドリブル成功率", 0, 100, 60),
        "デュエル勝率": st.slider("デュエル勝率", 0, 100, 55),
        "スプリント数": st.slider("スプリント数（0-100換算の簡易入力）", 0, 100, 60),
        "被突破数": st.slider("被突破数", 0, 10, 2),
    }

    st.divider()
    st.subheader("強化テーマ")
    goal_focus = st.multiselect(
        "目標に近いトレーニングキーワード",
        ["スプリント","ドリブル","パス","シュート","判断","視野","メンタル","クロス","守備","体幹"],
        default=[]
    )

st.header("100能力入力")
scores = {}

tabs = st.tabs(list(ABILITY_CATEGORIES.keys()))
for tab, (category, abilities) in zip(tabs, ABILITY_CATEGORIES.items()):
    with tab:
        cols = st.columns(3)
        for i, ab in enumerate(abilities):
            scores[ab] = cols[i % 3].slider(f"{ab}", 1, 5, 3, key=f"{category}_{ab}")

# =========================================================
# Calculation
# =========================================================

category_averages = calc_category_averages(scores)
match_iq = calc_match_iq(scores)
match_index = calc_match_index(match_metrics)
position_fit_main = calc_position_fit(scores, position, height, weight, phv_stage)
position_fit_all = {pos: calc_position_fit(scores, pos, height, weight, phv_stage) for pos in POSITION_WEIGHTS.keys()}
position_fit_df = pd.DataFrame(
    [{"ポジション": k, "適性": v} for k, v in position_fit_all.items()]
).sort_values("適性", ascending=False)

growth_df = calc_growth_projection(scores, age_stage, phv_stage, n_type, p_type, m_type)
priority_df = calc_training_priorities(scores, position, age_stage, phv_stage, n_type, p_type, m_type, match_metrics, goal_focus)
training_df = select_trainings_from_priorities(priority_df, top_n_abilities=5)
weekly_plan = generate_weekly_plan(training_df)
strengths_df, weaknesses_df = top_strengths_and_weaknesses(scores)
rating = calc_player_rating(scores, n_type, p_type, m_type, age_stage, phv_stage, height, weight, match_index)
relation_notes = relation_analysis(scores)

# =========================================================
# Output
# =========================================================

col1, col2, col3, col4 = st.columns(4)
col1.metric("PLAYER RATING", rating)
col2.metric("MATCH IQ", match_iq)
col3.metric("主ポジション適性", position_fit_main)
col4.metric("試合指数", match_index)

st.subheader("選手プロフィール")
st.write({
    "名前": player_name,
    "年齢": age,
    "年齢ステージ": age_stage,
    "身長": height,
    "体重": weight,
    "ポジション": position,
    "サブポジション": sub_position,
    "PHV": phv_stage,
    "神経タイプ": n_type,
    "フィジカルタイプ": p_type,
    "メンタルタイプ": m_type
})

st.subheader("能力カテゴリ平均")
cat_df = pd.DataFrame(
    [{"カテゴリ": k, "平均": v} for k, v in category_averages.items()]
)
st.dataframe(cat_df, use_container_width=True, hide_index=True)

c1, c2 = st.columns(2)
with c1:
    st.subheader("強みTOP5")
    st.dataframe(strengths_df, use_container_width=True, hide_index=True)
with c2:
    st.subheader("弱点TOP5")
    st.dataframe(weaknesses_df, use_container_width=True, hide_index=True)

st.subheader("関係性分析")
for note in relation_notes:
    st.write(f"- {note}")

st.subheader("ポジション適性ランキング")
st.dataframe(position_fit_df, use_container_width=True, hide_index=True)

st.subheader("成長予測TOP10")
st.dataframe(growth_df.head(10), use_container_width=True, hide_index=True)

st.subheader("優先能力TOP10")
st.dataframe(priority_df.head(10), use_container_width=True, hide_index=True)

st.subheader("AIトレーニング提案")
st.dataframe(training_df, use_container_width=True, hide_index=True)

st.subheader("カテゴリ別トレーニング")
for category in ["PHYSICAL", "TECHNICAL", "FOOTBALL_IQ", "MENTAL"]:
    with st.expander(category, expanded=True):
        cat_trainings = training_df[training_df["カテゴリ"] == category]["トレーニング"].tolist()
        if cat_trainings:
            for t in cat_trainings:
                st.write(f"- {t}")
        else:
            st.write("該当なし")

st.subheader("週間トレーニングプラン")
week_df = pd.DataFrame(
    [{"曜日": d, "メニュー": " / ".join(v)} for d, v in weekly_plan.items()]
)
st.dataframe(week_df, use_container_width=True, hide_index=True)

st.subheader("計算の考え方")
st.write("""
- 能力評価はそのまま保持し、係数は補正にのみ使う。
- トレーニング優先度 = 弱点度 × ポジション重要度 × 年齢係数 × PHV係数 × タイプ補正 × 試合補正 × 目標補正
- ポジション適性 = 能力 × 重み の合計を基礎に、身体補正を微調整で反映する。
- PLAYER RATING = 能力指数 × タイプ指数 × 身体発達補正 × 試合指数
""")

with st.expander("全トレーニングDB一覧"):
    for cat, items in TRAINING_DB.items():
        st.markdown(f"### {cat}")
        st.write(", ".join(items))









#################################################
# NPM → Ability Score変換
#################################################
ability_scores = defaultdict(float)

# ポジション重み
for ability, weight in POSITION_WEIGHTS.get(position, {}).items():
    ability_scores[ability] += weight * 10

# 神経タイプ補正
for ability, coef in N_BONUS.get(N_type, {}).items():
    ability_scores[ability] *= coef

# 身体タイプ補正
for ability, coef in P_BONUS.get(P_type, {}).items():
    ability_scores[ability] *= coef

# メンタル補正
for ability, coef in M_BONUS.get(M_type, {}).items():
    ability_scores[ability] *= coef


#年齢補正
age_stage = st.selectbox("年代カテゴリ", AGE_STAGE_OPTIONS)
phv_stage = st.selectbox("PHV段階", PHV_OPTIONS)

for ability in ability_scores:

    domain = ABILITY_TO_DOMAIN.get(ability)

    if domain:

        ability_scores[ability] *= AGE_DOMAIN_COEFFICIENTS[age_stage][domain]
        ability_scores[ability] *= PHV_DOMAIN_COEFFICIENTS[phv_stage][domain]




#################################################
# PHV計算
#################################################

st.header("PHV成長分析")

age = st.number_input("年齢", 8, 18)
height = st.number_input("身長(cm)", 120, 200)
weight = st.number_input("体重(kg)", 20, 100)
sitting_height = st.number_input("座高(cm)", 60, 110)

leg_length = height - sitting_height

PHV = (
    -9.236
    + (0.0002708 * (leg_length * sitting_height))
    - (0.001663 * (age * leg_length))
    + (0.007216 * (age * sitting_height))
    + (0.02292 * (weight / height))
)

st.subheader("PHV推定値")
st.write(round(PHV,2))

#################################################
# ポジション適正
#################################################

st.header("ポジション適正AI")

position_weights = {
    "FW": {"N3":2,"P1":2,"M4":2},
    "MF": {"N4":2,"P2":2,"M2":2},
    "DF": {"N2":2,"P3":2,"M5":2},
    "WG": {"N1":2,"P1":2,"M4":2},
    "SB": {"N1":2,"P2":2,"M3":2}
}

position_scores = {}

for pos,weights in position_weights.items():

    score = 0

    if N_type in weights:
        score += weights[N_type]

    if P_type in weights:
        score += weights[P_type]

    if M_type in weights:
        score += weights[M_type]

    position_scores[pos] = score

best_position = max(position_scores,key=position_scores.get)

st.subheader("推奨ポジション")
st.write(best_position)

#################################################
# 試合データ
#################################################

st.header("試合パフォーマンス")

sprint = st.slider("スプリント回数",0,50)
pass_success = st.slider("パス成功率",0,100)
duel = st.slider("デュエル勝率",0,100)
distance = st.slider("走行距離(km)",0,15)

performance_score = (
    sprint*0.2 +
    pass_success*0.3 +
    duel*0.3 +
    distance*5
)

st.subheader("試合評価スコア")
st.write(round(performance_score,1))


#試合データ補正
match_data = {
    "ドリブル成功率": pass_success,
    "パス成功率": pass_success,
    "デュエル勝率": duel,
    "スプリント数": sprint
}

for metric,value in match_data.items():

    abilities = MATCH_METRIC_TO_ABILITIES.get(metric,[])

    for a in abilities:
        ability_scores[a] += value * 0.1


#弱点能力抽出
sorted_abilities = sorted(
    ability_scores.items(),
    key=lambda x:x[1]
)

weak_abilities = [a for a,_ in sorted_abilities[:10]]




#################################################
# AIトレーニング生成
#################################################

st.header("AI週間トレーニング")

training = []

if N_type == "N1":
    training.append("HIITスプリント")

if P_type == "P1":
    training.append("加速トレーニング")

if M_type == "M3":
    training.append("反復基礎トレーニング")

training.append("戦術理解")
training.append("体幹トレーニング")

days = ["月","火","水","木","金","土"]

schedule = {}

for day in days:

    schedule[day] = training

df = pd.DataFrame(schedule)

st.dataframe(df)


###################
training_plan = []

for ability in weak_abilities:

    trainings = ABILITY_TO_TRAININGS.get(ability,[])

    training_plan.extend(trainings)

training_plan = list(set(training_plan))[:12]


days = ["月","火","水","木","金","土"]

schedule = {}

i = 0

for day in days:

    schedule[day] = training_plan[i:i+2]

    i += 2

df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in schedule.items()]))

st.subheader("AI週間トレーニングメニュー")

st.dataframe(df)




