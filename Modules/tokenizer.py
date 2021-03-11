from konlpy.tag import Okt
from Modules import sys, _CoreModules


class SchoolRuleTokenizer(_CoreModules):
    """
    학칙을 토큰화 시키는 클래스
    """

    def __init__(self):
        _CoreModules.__init__(self)

        self.IDENTIFY_NAME = "SchoolRuleTokenizer"

        self.OKT = Okt()

    def tokenizer(self, sentence: str):
        response = None
        try:
            # print(self.OKT.phrases(sentence))

            middle_class_start_no = 0
            middle_class_end_no = None

            title_start_no = None
            title_end_no = None

            content_start_no = None
            for char_no in range(0, len(sentence)):
                if sentence[char_no] == "(" and title_start_no is None:
                    middle_class_end_no = char_no
                    title_start_no = char_no + 1

                if sentence[char_no] == ")" and title_end_no is None:
                    title_end_no = char_no
                    content_start_no = char_no + 1

            middle_class_no = str(sentence[middle_class_start_no:middle_class_end_no]).strip()
            small_class_no = None

            title = str(sentence[title_start_no:title_end_no]).strip()
            content = str(sentence[content_start_no:]).strip()

            if "의" in middle_class_no:
                small_class_no = middle_class_no.split("의")[1]

            response = {
                "조": middle_class_no,
                "항": small_class_no is None and 1 or small_class_no,
                "주제": title,
                "주제 토큰": set(self.OKT.phrases(title)),
                "내용": content,
                "내용 토큰": set(self.OKT.phrases(content))
            }

            # response = {
            #     "MIDDLE NO": middle_class_no,
            #     "SMALL NO": small_class_no,
            #     "TITLE": title,
            #     "TITLE TOKEN": set(self.OKT.phrases(title)),
            #     "CONTENT": content,
            #     "CONTENT TOKEN": set(self.OKT.phrases(content))
            # }
        except:
            self.record_log(self.IDENTIFY_NAME, sys.exc_info())
            response = None
        finally:
            return response
