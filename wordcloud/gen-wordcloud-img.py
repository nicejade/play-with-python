import jieba
import wordcloud
import PIL.Image as image
import numpy as np

relative_path = './wordcloud/'
target_path = 'target.txt'

def get_jieba_words():
    content_str = open(relative_path + target_path, 'r', encoding='utf-8').read()
    return jieba.lcut(content_str)

def get_high_frequency_word(param_list):
    exclude_words_list = ['我们', '你们', '可以']
    counts_dict = {}
    for word in param_list:
        if len(word) == 1:
            continue
        else:
            is_word_exist = False
            for ex_word in exclude_words_list:
                if ex_word in word:
                    is_word_exist = True
            if not is_word_exist:
                if not word.isdigit():
                    count = counts_dict.get(word, 0) + 1
                    counts_dict[word] = count
    return sorted(counts_dict.items(), key=lambda x: x[1], reverse=True)

def get_cloud_words(param_list):
    result_str = ''
    for item in param_list[0:100]:
        occur_count = item[1]
        for _ in range(occur_count):
            result_str = result_str + ' ' + item[0]
    return result_str

def gen_and_save_wordcloud_img(param_str):
    mask = np.array(image.open(relative_path + "style.jpg"))
    wc = wordcloud.WordCloud(width=1430, height=646, background_color="rgba(255, 255, 255, 0)",
                            mode="RGBA", font_path=relative_path + 'MSYH.TTC', collocations=False, max_words=100, mask=mask)
    # 调用词云对象的 generate 方法，将文本传入
    wc.generate(param_str)
    # 将生成的词云以图片文件格式，保存在当前目录
    wc.to_file(relative_path + 'output-result.png')

jieba_words_list = get_jieba_words()
print('所获得 jieba 分词个数为：', len(jieba_words_list))

high_frequency_word_list = get_high_frequency_word(jieba_words_list)
print('所得高频分词前 100 分别是：', high_frequency_word_list[0:100])

cloud_words_str = get_cloud_words(high_frequency_word_list)
gen_and_save_wordcloud_img(cloud_words_str)
print('已成功生成「词云图」并保存在当前目录.')