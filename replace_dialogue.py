#!/usr/bin/env python3
"""Replace Chinese dialogue with original English in all v2 prompt files."""
import os

BASE = "/Users/mengmengjiang/sinclair-design"

# (chinese, english_for_txt, english_for_html)
# txt files: use regular apostrophes
# html files: use \' for apostrophes inside JS single-quoted strings
MAP = [
    # ── EP01 ──
    ("西娅，快许愿吧。",
     "Thea, make a wish!",
     "Thea, make a wish!"),
    ("亲爱的，我来帮你拍照。",
     "Babe, let me take a picture for you.",
     "Babe, let me take a picture for you."),
    ("凯和西娅小时候感情就好，现在家族联姻，看起来更甜蜜了，听说下周就要结婚了，真羡慕啊。",
     "Kai and Thea have been inseparable since they were kids. Now that they're finally getting married, they look happier than ever. I heard the wedding is next week. Honestly, I'm jealous.",
     "Kai and Thea have been inseparable since they were kids. Now that they\\'re finally getting married, they look happier than ever. I heard the wedding is next week. Honestly, I\\'m jealous."),
    ("羡慕？你还不知道吧，听说凯在外面早就养了个小的了……",
     "You don't know, do you? Word is Kai has another woman on the side. And it's been going on for a while now.",
     "You don\\'t know, do you? Word is Kai has another woman on the side. And it\\'s been going on for a while now."),
    ("辛迪，怎么了？.....好.....好的，我马上就到。",
     "Cindy, what's wrong? Okay. Alright. I'll be right there.",
     "Cindy, what\\'s wrong? Okay. Alright. I\\'ll be right there."),
    ("西娅，辛迪有点不舒服，我得马上过去。你自己切蛋糕吧。",
     "Cindy is not feeling well. I gotta check on her. Sorry babe, you have to cut the cake without me.",
     "Cindy is not feeling well. I gotta check on her. Sorry babe, you have to cut the cake without me."),
    ("又是辛迪，为什么每一次她一找你，你就立马抛下我赶过去？",
     "Cindy again. Why do you have to drop everything every time she calls?",
     "Cindy again. Why do you have to drop everything every time she calls?"),
    ("西娅，你是贵族该学会大度，而且，你有那么多朋友陪着，她一个贫民区出来的孤儿，无依无靠只有我。更何况，她小时候还救过我的命！",
     "Thea, you have to understand. You've got all these friends here. She's got nobody but me. And she saved my life when we were kids.",
     "Thea, you have to understand. You\\'ve got all these friends here. She\\'s got nobody but me. And she saved my life when we were kids."),
    ("你又拿这个压我！今天是我的生日，她一个电话就把你叫走了，你们的关系真的正常吗？",
     "There you go again. Today is my birthday! One phone call from her and you're leaving me here alone. Is that really normal?",
     "There you go again. Today is my birthday! One phone call from her and you\\'re leaving me here alone. Is that really normal?"),
    ("闭嘴！西娅，你真是被宠坏了，辛迪比你懂事多了，等你能冷静了我们再沟通。",
     "Shut up! Thea, you're so damn spoiled. Cindy's far more reasonable than you are. We'll talk when you've calmed down.",
     "Shut up! Thea, you\\'re so damn spoiled. Cindy\\'s far more reasonable than you are. We\\'ll talk when you\\'ve calmed down."),
    ("不许走！凯，你今天要是敢离开这里半步，我们立刻就分手！",
     "Don't you walk away from me! Kai, if you walk out of here today, we're done.",
     "Don\\'t you walk away from me! Kai, if you walk out of here today, we\\'re done."),
    ("让开！分手？呵呵，先问问你家里同意吗？哼，别拿分手威胁我，我是自由的！",
     "You want to break up? As if your family would let that happen. Stop trying to control me. I can do whatever I want.",
     "You want to break up? As if your family would let that happen. Stop trying to control me. I can do whatever I want."),
    # ── EP02 ──
    ("哈哈哈，西娅，让我猜猜，你许了什么愿望？是不是想快点成年，完成和凯的婚约？",
     "Thea, what did you wish for? Let me guess. You want to grow up faster so you can marry Kai, right?",
     "Thea, what did you wish for? Let me guess. You want to grow up faster so you can marry Kai, right?"),
    ("你说什么呢，我才没有！",
     "What are you talking about? That's not it.",
     "What are you talking about? That\\'s not it."),
    ("我们的婚约可是从小就定下的，西娅，你不想嫁给我，难道想嫁给别人？",
     "We were betrothed since we were kids. What, you don't want to marry me anymore? Are you planning to marry someone else?",
     "We were betrothed since we were kids. What, you don\\'t want to marry me anymore? Are you planning to marry someone else?"),
    ("西娅，我将你让给他，他竟然敢这么对你！",
     "How dares he treat you like this?",
     "How dares he treat you like this?"),
    ("基恩，我就知道，我的生日你一定会来，今年不会又是送了礼物就走吧。",
     "Keane! I knew you'd never miss my birthday. You're not going to just drop off a gift and disappear again this year, are you?",
     "Keane! I knew you\\'d never miss my birthday. You\\'re not going to just drop off a gift and disappear again this year, are you?"),
    ("你知道我不喜欢热闹。",
     "You know I don't like crowds.",
     "You know I don\\'t like crowds."),
    ("谢谢，我能现在就打开看吗？",
     "Thank you! Can I open it now?",
     "Thank you! Can I open it now?"),
    ("当然。",
     "Of course.",
     "Of course."),
    ("哇，是莱卡镜头！基恩，你对我真好，总是知道我最喜欢什么！",
     "Oh my God. Keane, you're so good to me. You always know exactly what I want.",
     "Oh my God. Keane, you\\'re so good to me. You always know exactly what I want."),
    ("你的喜好，我当然要记得了，试一试吧，大摄影师。",
     "Go on, big-shot photographer, give it a try.",
     "Go on, big-shot photographer, give it a try."),
    # ── EP03 ──
    ("怎么了？是不喜欢那边的景色吗？",
     "What's wrong? What did you see?",
     "What\\'s wrong? What did you see?"),
    ("上帝啊，我看到了什么！",
     "I can't believe it. How can he do this to me?",
     "I can\\'t believe it. How can he do this to me?"),
    ("凯竟然这样明目张胆的背叛我，他果然一直在骗我，难怪每次辛迪只要一个电话，就能马上把他叫走！",
     "Kai's been cheating on me! He's been lying to me this whole time!",
     "Kai\\'s been cheating on me! He\\'s been lying to me this whole time!"),
    ("西娅，也许我们都看错了？凯他怎么会这么做？",
     "Thea... maybe we got it wrong. Kai would never do something like that.",
     "Thea... maybe we got it wrong. Kai would never do something like that."),
    ("凯他出轨了！我都看见了！可是我们下周就要结婚了！不，我绝不能和这样的男人结婚，我现在就要找他退婚！",
     "I saw him kissing Cindy with my own eyes! I can't marry a man like this. I'm calling off the engagement.",
     "I saw him kissing Cindy with my own eyes! I can\\'t marry a man like this. I\\'m calling off the engagement."),
    ("西娅你冷静一点，辛克莱家族和兰开斯特家是世交，家族利益捆绑得很深，这婚不是你想退，家里人就能答应的，你要不……忍忍吧？",
     "Thea, calm down. The Sinclairs and the Lancasters go way back. You can't just call off the wedding by yourself. Your family won't allow it. Maybe you should just put up with it.",
     "Thea, calm down. The Sinclairs and the Lancasters go way back. You can\\'t just call off the wedding by yourself. Your family won\\'t allow it. Maybe you should just put up with it."),
    ("忍？凭什么总是我忍，从两年前辛迪出现后，凯和我之间的感情就变了！其实，我一直分不清，对他是只有哥哥的感情，还是真正的爱情，但是我们从小就有婚约啊，我怎么能忍受的了他这样的背叛和羞辱！",
     "Why should I be the one who has to endure it? I am his betrothed! How can he humiliate me like this? Ever since Cindy showed up two years ago, everything between Kai and me has changed. But honestly, I've never even been so sure whether what I feel for him is love, or just sisterly affection.",
     "Why should I be the one who has to endure it? I am his betrothed! How can he humiliate me like this? Ever since Cindy showed up two years ago, everything between Kai and me has changed. But honestly, I\\'ve never even been so sure whether what I feel for him is love, or just sisterly affection."),
    ("我的小西娅，冷静，总会有办法的。真希望我在此时此刻能够帮到你。",
     "Thea. Calm down. You can work it out. I just wish I could do something for you right now.",
     "Thea. Calm down. You can work it out. I just wish I could do something for you right now."),
    ("你真的愿意帮我吗？",
     "Do you really want to help me?",
     "Do you really want to help me?"),
    ("你也姓兰开斯特，不如，你和我结婚吧。",
     "You're a Lancaster too. Why don't you marry me instead?",
     "You\\'re a Lancaster too. Why don\\'t you marry me instead?"),
    ("西娅，和你有婚约的，是我的亲弟弟凯！",
     "Thea, you're engaged to my brother.",
     "Thea, you\\'re engaged to my brother."),
]

txt_files = [
    f"{BASE}/辛克莱别墅_视频提示词_v2_EP01.txt",
    f"{BASE}/辛克莱别墅_视频提示词_v2_EP02.txt",
    f"{BASE}/辛克莱别墅_视频提示词_v2_EP03.txt",
    f"{BASE}/辛克莱别墅_视频提示词_v2_完整版.txt",
]
html_file = f"{BASE}/辛克莱别墅_视频提示词_v2.html"

# Process .txt files (use plain English)
for fp in txt_files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    count = 0
    for cn, en_txt, _ in MAP:
        if cn in content:
            content = content.replace(cn, en_txt)
            count += 1
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"TXT DONE: {os.path.basename(fp)} — {count} replacements")

# Process HTML file (use JS-escaped English)
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()
count = 0
for cn, _, en_html in MAP:
    if cn in content:
        content = content.replace(cn, en_html)
        count += 1
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"HTML DONE: {os.path.basename(html_file)} — {count} replacements")
