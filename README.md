# ChineseWordSegmentation
该项目中介绍了jieba,hanlp,snownlp,nlpir,pkuseg,thulac几个常用分词工具，并结合其分词性能与时间效率做了比较

# 实验流程介绍

> 分词工具安装

> [数据下载](http://sighan.cs.uchicago.edu/bakeoff2005/)

> 实验

## 分词工具安装及使用

> 1、[jieba](https://github.com/fxsjy/jieba)
```python
pip3 install jieba 
```
> 2、[hanlp](https://github.com/hankcs/HanLP)
```python
pip3 install hanlp
```
> 3、[pkuseg](https://github.com/lancopku/PKUSeg-python)
```python
pip3 install pkuseg
```
> 4、[thulac](https://github.com/thunlp/THULAC-Python)
```python
pip3 install thulac
```
> 5、[snownlp](https://github.com/isnowfy/snownlp)
```python
pip3 install snownlp
```
> 6、[nlpir](https://github.com/NLPIR-team/NLPIR)
```python
pip3 install pynlpir
```
## data目录结构
主要和本项目相关的目录，可以直接下载使用上边的[数据集](http://sighan.cs.uchicago.edu/bakeoff2005/)
data<br/>
　-icwb2<br/>
　　-testing<br/>
    -gold<br/>
    -segment<br/>
    
## 项目运行
该项目共两个参数，第一个参数为分词工具，其范围[hanlp,jieba,snownlp,nlpir,pkuseg,thulac]
第二个参数为分词的数据集[cityu, as, msr, pku]
'''
python segment_score.py jieba as
'''
