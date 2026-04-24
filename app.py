import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="중국어I 중간고사 정복", layout="centered")

# --- 중국어I 데이터베이스 (시험지 & 범위자료 100% 반영) ---
if 'quiz_data' not in st.session_state:
    db = [
        # [문화 및 언어 지식]
        {"q": "중국 표준어인 '보통화'의 발음 기준이 되는 지역은?", "a": "베이징", "type": "choice", "options": ["베이징", "상하이", "광둥", "산둥"]},
        {"q": "중국에서 사용하는 간략화된 한자의 명칭은?", "a": "간화자", "type": "choice", "options": ["간화자", "번체자", "약자", "고체"]},
        {"q": "중국 국기 '오성홍기'의 큰 별은 무엇을 상징하나요?", "a": "중국 공산당", "type": "choice", "options": ["중국 공산당", "노동자", "농민", "지식인"]},
        {"q": "중국 서체 중 획을 최대한 줄여 예술성이 뛰어난 흘림체는?", "a": "초서", "type": "choice", "options": ["초서", "해서", "행서", "예서"]},
        {"q": "판다(熊猫)가 주로 서식하며 생태공원이 조성된 지역은?", "a": "청두", "type": "choice", "options": ["청두", "베이징", "시안", "광저우"]},
        
        # [한어병음 및 성조]
        {"q": "성조 변화: 3성 + 3성이 만날 때 앞의 3성은 몇 성으로 발음?", "a": "2성", "type": "choice", "options": ["1성", "2성", "4성", "경성"]},
        {"q": "māma 에서 두 번째 'ma'의 성조는?", "a": "경성", "type": "choice", "options": ["1성", "2성", "3성", "경성"]},
        {"q": "한어병음 'j' 뒤에 'u'가 올 때 점 두 개(ü)는 어떻게 하나요?", "a": "생략한다", "type": "choice", "options": ["생략한다", "그대로 둔다", "다른 글자로 바꾼다"]},

        # [어휘: 병음 -> 뜻 (주관식 한글입력)]
        {"q": "túshūguǎn", "a": "도서관", "type": "text"},
        {"q": "nóngcūn", "a": "농촌", "type": "text"},
        {"q": "chúfáng", "a": "주방", "type": "text"},
        {"q": "huānyíng", "a": "환영하다", "type": "text"},
        {"q": "zhǔnbèi", "a": "준비하다", "type": "text"},
        {"q": "bàba", "a": "아버지", "type": "text"},
        {"q": "māma", "a": "어머니", "type": "text"},
        {"q": "jiějie", "a": "누나", "type": "text"},
        {"q": "dìdi", "a": "남동생", "type": "text"},
        {"q": "yéye", "a": "할아버지", "type": "text"},
        {"q": "māo", "a": "고양이", "type": "text"},
        {"q": "gǒu", "a": "강아지", "type": "text"},
        {"q": "niǎo", "a": "새", "type": "text"},

        # [어휘: 뜻 -> 병음 (객관식 선택)]
        {"q": "뜻: '만리장성'", "a": "Chángchéng", "type": "choice", "options": ["Chángchéng", "Xióngmāo", "Zhájiàngmiàn", "Putonghua"]},
        {"q": "뜻: '안녕하세요(여러분)'", "a": "Dàjiā hǎo", "type": "choice", "options": ["Nǐ hǎo", "Dàjiā hǎo", "Lǎoshī hǎo", "Zǎoshang hǎo"]},
        {"q": "뜻: '괜찮아(사과에 대한 응답)'", "a": "Méi guānxi", "type": "choice", "options": ["Méi guānxi", "Bú kèqi", "Xièxie", "Bú xiè"]},
        {"q": "뜻: '천만에요(감사에 대한 응답)'", "a": "Bú kèqi", "type": "choice", "options": ["Méi guānxi", "Bú kèqi", "Duìbuqǐ", "Zàijiàn"]},
        {"q": "뜻: '내일 봐'", "a": "Míngtiān jiàn", "type": "choice", "options": ["Míngtiān jiàn", "Zàijiàn", "Wǎnshang hǎo", "Nǐ hǎo ma"]}
    ]
    st.session_state.quiz_data = db
    st.session_state.indices = random.sample(range(len(db)), len(db))
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.is_correct = False

def restart():
    st.session_state.indices = random.sample(range(len(st.session_state.quiz_data)), len(st.session_state.quiz_data))
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.answered = False

def next_question():
    st.session_state.current_idx += 1
    st.session_state.answered = False

# UI
st.title("🇨🇳 중국어I 중간고사 정복")
st.progress(st.session_state.current_idx / len(st.session_state.quiz_data))

if st.session_state.current_idx < len(st.session_state.indices):
    q_data = st.session_state.quiz_data[st.session_state.indices[st.session_state.current_idx]]
    st.subheader(f"Q{st.session_state.current_idx + 1}. {q_data['q']}")

    if not st.session_state.answered:
        if q_data['type'] == "choice":
            for opt in q_data['options']:
                if st.button(opt, use_container_width=True):
                    st.session_state.answered = True
                    st.session_state.is_correct = (opt == q_data['a'])
                    if st.session_state.is_correct: st.session_state.score += 1
                    st.rerun()
        else:
            ans = st.text_input("한국어 뜻 입력:", key=f"ans_{st.session_state.current_idx}")
            if st.button("확인", use_container_width=True):
                if ans:
                    st.session_state.answered = True
                    st.session_state.is_correct = (ans.replace(" ","") in q_data['a'].replace(" ",""))
                    if st.session_state.is_correct: st.session_state.score += 1
                    st.rerun()
    else:
        if st.session_state.is_correct: st.success("정답입니다! ⭕")
        else: st.error(f"틀렸습니다. 정답은 [{q_data['a']}] 입니다. ❌")
        if st.button("다음 문제로 ➡️", on_click=next_question, use_container_width=True):
            st.rerun()
else:
    st.balloons()
    st.header("🎊 전 범위 정복 완료!")
    st.metric("최종 점수", f"{st.session_state.score} / {len(st.session_state.quiz_data)}")
    if st.button("다시 하기 (순서 무작위)", on_click=restart, use_container_width=True):
        st.rerun()

