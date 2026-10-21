# -*- coding: utf-8 -*-
"""2026년 6월 고1 학력평가(부산광역시 교육청) 22·23·24·32번 본문 (36번은 단어표 범위 밖이라 뺌)
원본: iCloud Drive/송우고1-2 2606 시험범위.pdf (WORKBOOK 문장별 영문+해석)"""

TITLE_EN = "2026 6월 고1 학력평가"
TITLE_KO = "22 · 23 · 24 · 32번"

# (sid, 영어 문장, 한국어 해석)
S = [
 ('s1', 'Suppose you have been working on the solution to a challenging technological problem for many years.', '당신이 수년간 어려운 기술 문제에 대한 해결책을 연구해 왔다고 가정해 보라.'),
 ('s2', 'Let’s also suppose that you have been paying attention to whatever else you have encountered that might be related to the problem.', '또한 그 문제와 관련이 있을지도 모르는, 당신이 마주해 온 다른 모든 것에도 주의를 기울여 왔다고 가정해 보자.'),
 ('s3', 'In that case, chances are that creative solutions to the problem could suddenly pop up in your mind when you are relaxed.', '그런 경우, 당신이 편안할 때, 아마도 그 문제에 대한 창의적인 해결책이 갑자기 떠오를 것이다.'),
 ('s4', 'Such “eureka moments” (when great insights lead to discovery or invention) often take place at unexpected times.', '그러한 ‘유레카 순간’(훌륭한 통찰력이 발견이나 발명으로 이어질 때)은 종종 예상치 못한 때 일어난다.'),
 ('s5', 'To enhance spontaneous creativity, therefore, one must pay attention to the things that could potentially lead to valuable outcomes.', '따라서, 자연 발생적인 창의성을 키우려면, 잠재적으로 가치 있는 결과로 이어질 수 있는 것들에 주의를 기울여야 한다.'),
 ('s6', 'This does not mean that you must narrow down your interest to one specific topic.', '이는 당신의 관심을 특정 주제에 국한해야 한다는 것을 의미하지 않는다.'),
 ('s7', 'On the contrary, breadth of experience is the key to creativity.', '반대로, 경험의 폭이 창의성의 핵심이다.'),
 ('s8', 'If your experience is limited to a narrow range of topics, then the scope of your imagination will likewise be narrow, which would be harmful to creativity.', '경험이 좁은 범위의 주제로 국한된다면, 상상력의 범위가 마찬가지로 좁아질 것이고, 이는 창의성에 해로울 것이다.'),
 ('s9', 'Shame is about who we are, and guilt is about our behaviors.', '수치심은 우리가 누구인가에 관한 것이고, 죄책감은 우리의 행동들에 관한 것이다.'),
 ('s10', 'We feel guilty when we hold up something we’ve done or failed to do against the kind of person we want to be.', '우리가 했거나 하지 못한 것을 우리가 되고자 하는 유형의 사람에 견줄 때 우리는 죄책감을 느낀다.'),
 ('s11', 'It’s an uncomfortable feeling, but one that’s helpful.', '그것은 불편한 감정이지만, 도움이 되는 것이다.'),
 ('s12', 'When we apologize for something we’ve done, make amends to others, or change a behavior that we don’t feel good about, guilt is most often the motivator.', '우리가 한 것에 대해 사과하거나, 다른 이에게 보상하거나, 좋다고 느끼지 않는 행동을 바꿀 때, 죄책감이 대체로 동기 요인이다.'),
 ('s13', 'Guilt is just as powerful as shame, but its effect is often positive while shame often is destructive.', '죄책감은 수치심만큼이나 강력하지만, 수치심은 종종 파괴적인 데 반해 그것(죄책감)의 효과는 종종 긍정적이다.'),
 ('s14', 'When we see people apologize, make amends, or replace negative behaviors with more positive ones, guilt is often the motivator, not shame.', '우리는 누군가가 사과하거나, 보상하거나, 부정적 행동을 더 긍정적인 행동으로 바꾸는 것을 볼 때, 죄책감은 종종 동기 요인이 되지만, 수치심은 아니다.'),
 ('s15', 'In fact, in my research, I found that shame corrodes the part of us that believes we can change and do better.', '실제로, 나의 연구에서, 수치심은 우리가 변하고 더 나아질 수 있다고 믿는 우리의 일부를 좀먹는다는 것을 발견했다.'),
 ('s16', 'Let’s look at what is occurring in your brain when scrolling on social media, a quick dopamine activity.', '소셜 미디어상에서 스크롤 할 때 당신의 뇌에서 일어나고 있는 일, 즉 빠른 도파민 활동을 살펴보자.'),
 ('s17', 'You open your social media apps and immediately you notice you feel really good, your dopamine levels increase incredibly fast and pleasure is experienced in your brain.', '당신은 소셜 미디어 앱을 열고 당신이 정말 기분이 좋다는 것을 즉시 알아차리게 되며, 당신의 도파민 수치는 믿을 수 없이 빠르게 증가하여 쾌락이 뇌에서 경험된다.'),
 ('s18', 'The challenge this creates is as with everything in our universe: as the laws of physics explain, ‘what goes up, must come down’.', '이것(도파민 급증)이 만들어 내는 난제는 우리 우주의 모든 것들과 마찬가지이다. 즉, 물리학 법칙이 설명하듯이, ‘올라가는 것은, 반드시 내려와야 한다.’'),
 ('s19', 'Your brain and body are always seeking something called ‘homeostasis’, which simply means balance.', '당신의 뇌와 몸은 ‘항상성’이라고 불리는 어떤 것을 항상 추구하고 있는데, 그것은 단순히 균형을 의미한다.'),
 ('s20', 'With this in mind, when dopamine levels increase incredibly fast when scrolling social media, the brain then thinks, ‘Wow, how are my dopamine levels so high?’', '이것을 염두에 두고, 소셜 미디어를 스크롤 할 때 도파민 수치가 믿을 수 없이 빠르게 증가하면, 뇌는 그때 ‘와, 내 도파민 수치가 어떻게 이렇게 높지?’라고 생각한다.'),
 ('s21', 'In order to achieve homeostasis, or balance, the dopamine then has to quickly drop an equal amount below your baseline level in order to rebalance, making you feel even worse than before you started scrolling.', '항상성, 즉 균형을 이루기 위해서, 그때 도파민은 다시 균형을 맞추기 위해 당신의 기준선 수치 아래로 동일한 양만큼 빠르게 떨어져야 하고, 스크롤을 시작하기 전보다 당신을 훨씬 더 기분이 나쁘게 만든다.'),
 ('s22', 'Do you always study in the same spot? Don’t.', '항상 같은 장소에서 공부하는가? 그러지 마라.'),
 ('s23', 'If you study in different places, that helps create variety, and that rich experience can reinforce what you are learning.', '여러 장소에서 공부하면, 그것은 다양성을 만들도록 돕고, 그러한 풍부한 경험은 당신이 학습하고 있는 것을 강화할 수 있다.'),
 ('s24', 'When several college students told us they did school work in different places rather than in some favorite nook, that habit reflected the research on learning.', '몇몇 대학생들이 좋아하는 어떤 구석진 곳에서보다는 여러 장소에서 학교 과제를 한다고 우리에게 말했을 때, 그 습관은 학습에 관한 연구를 반영했다.'),
 ('s25', 'Numerous experiments have found that if learners simply study in at least two different places, they are more likely to recall the material.', '수많은 실험은 학습자가 최소 두 곳 이상의 다른 장소에서 단지 공부하기만 해도, 학습 자료를 기억할 가능성이 더 높다는 것을 발견했다.'),
 ('s26', 'In one of the first such trials, two different groups studied a list of words.', '그러한 초기 실험들 중 하나에서 두 개의 다른 집단이 하나의 단어 목록을 공부하였다.'),
 ('s27', 'Some students returned to the same room twice while their counterparts spent the same amount of time divided between two locations.', '일부 학생들은 같은 방으로 두 번 돌아왔지만, 상대 집단은 두 장소에서 동일하게 나뉜 시간을 보냈다.'),
 ('s28', 'When asked to recall as many words on the list as possible, those who had moved around did far better.', '목록에 있는 가능한 한 많은 단어를 기억해 보라고 요청받았을 때, 장소를 옮겨 다닌 학생들이 훨씬 더 잘했다.'),
 ('s29', 'Variety creates rich association, even when those connections form in the background, totally outside of what we are consciously thinking.', '다양성은 풍부한 연상을 만들어 내는데, 이러한 연결들이 배경에서, 즉 우리가 의식적으로 생각하고 있는 것의 완전히 바깥에서, 형성될 때조차도 (그러하다).'),
]

# 문항별 문단 (본문 탭·통문제 렌더링용)
PARAS = [
    ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8'],
    ['s9', 's10', 's11', 's12', 's13', 's14', 's15'],
    ['s16', 's17', 's18', 's19', 's20', 's21'],
    ['s22', 's23', 's24', 's25', 's26', 's27', 's28', 's29'],
]

LABELS = ['22', '23', '24', '32']   # PARAS와 같은 순서의 문항 번호
