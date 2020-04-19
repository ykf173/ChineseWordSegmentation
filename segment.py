import json
import time
import jieba
import hanlp
import pkuseg
import thulac
from snownlp import SnowNLP
import pynlpir
import sys

class Segment:
    def jieba_segment(self, sentence):
        seg_list = jieba.cut(sentence, cut_all=False)
        sentence = ' '.join(seg_list)
        return sentence

    def hanlp_segment(self, han_tokenizer, sentence):
        # hanlp分词
        sentence = han_tokenizer(sentence)
        return ' '.join(sentence)

    def thulac_segment(self, thu, sentence):
        # thulac 分词
        sentence = thu.cut(sentence, text=True)  # 进行一句话分词
        #cut_f(输入文件, 输出文件)
        return ' '.join(sentence)

    def pkuseg_segment(self, sentence):
        seg = pkuseg.pkuseg(postag=False)  # 以默认配置加载模型
        sentence = seg.cut(sentence)  # 进行分词
        return ' '.join(sentence)

    def pynlpir_segment(self, sentence):
        # pynlpir分词
        pynlpir.open()
        sentence = pynlpir.segment(sentence, pos_tagging=False)
        pynlpir.close()
        return ' '.join(sentence)

    def snownlp_segment(self, sentence):
        # snownlp分词
        # unicode_sentence = sentence.decode('gbk')
        sentence = SnowNLP(sentence).words
        return ' '.join(sentence)


def test():
    test_path = 'data/icwb2/cityu_test.utf8'
    seg_path = 'data/icwb2/segment/hanlp/cityu_segment_test.utf8'
    seg = Segment()
    count = 0
    #thu = thulac.thulac(seg_only = True)
    with open(test_path, 'r', encoding='utf-8-sig') as f_r:  ##注意，这里的编码，utf-8 bom会在文件头加\ufeff，否则会有小问题
        with open(seg_path, 'w', encoding='utf-8') as f_w:
            for line_sentence in f_r:
                # line_sentence = getattr(Segment(), segment_func)(line_sentence)#根据参数调用不同分词工具
                # if 'snow' in segment_func:
                sentence = seg.pkuseg_segment(line_sentence)
                if count%20 == 0:
                    print(count/20)
                    print(sentence)
                f_w.write(sentence+'\n')
                count += 1

if __name__ == '__main__':

    data = {1:'cityu', 2:'as', 3:'msr', 4:'pku'}
    index = int(sys.argv[2])
    segment_tool = sys.argv[1]

    test_path = 'data/icwb2/' + data[index] + '_test.utf8'
    seg_path = 'data/icwb2/segment/' + segment_tool + '/' + data[index] + '_segment_test.utf8'

    time_statistic = 'data/time_statistic/' + segment_tool + '_time_statistic.txt'

    print("python argv[1]->segment_tool  argv[2]->file[cityu, as, msr, pku]", data)
    if segment_tool == 'jieba':
        jieba.enable_paddle()  # 启动paddle模式。 0.40版之后开始支持，早期版本不支持


    #eval('test_path' + sys.argv[2])字符串转变量
    #eval('seg_path' + sys.argv[2])

    print(test_path)
    print(seg_path)

    segment_func = segment_tool + '_segment'
    start = time.perf_counter()

    if 'thulac' in segment_func:
        thu = thulac.thulac(seg_only=True)
    if  'hanlp' in segment_func:
        han_tokenizer = hanlp.load('PKU_NAME_MERGED_SIX_MONTHS_CONVSEG')
    with open(test_path, 'r', encoding='utf-8-sig') as f_r:  ##注意，这里的编码，utf-8 bom会在文件头加\ufeff，否则会有小问题
        with open(seg_path, 'w', encoding='utf-8') as f_w:
            for line_sentence in f_r:
                if 'thulac' in segment_func:
                    line_sentence = getattr(Segment(), segment_func)(thu, line_sentence)  # 根据参数调用不同分词工具
                elif 'hanlp' in segment_func:
                    line_sentence = getattr(Segment(), segment_func)(han_tokenizer, line_sentence)
                else:
                    line_sentence = getattr(Segment(), segment_func)(line_sentence)#根据参数调用不同分词工具
                if 'snow' in segment_func:
                    f_w.write(line_sentence+'\n')
                else:
                    f_w.write(line_sentence)
    end = time.perf_counter()

    with open(time_statistic, 'a', encoding='utf-8') as f_time:
        print('分词运行时间：', end-start)
        dic = {}
        dic[test_path[11:-10]] = end-start
        f_time.write(json.dumps(dic)+'\n')

