import os
import sys
import datetime
from typing import Dict

# 모듈 패키지 경로를 프로젝트 전역 변수에 강제로 선언
sys.path.append(os.getcwd())


class _CoreModules:
    # 루트 경로 설정
    # PATH: Dict[str, str] = {"ROOT": os.getcwd()}
    PATH: Dict[str, str] = {"ROOT": "/Applications/PythonS/SchoolRuler"}

    def __init__(self):
        """
        클래스 생성자
        """
        # 날짜, 시간 마크 생성
        self.DATE_MARK = datetime.datetime.strftime(self.current_time(), "%Y%m%d")
        self.TIME_MARK = datetime.datetime.strftime(self.current_time(), "%H%M%S")

        # 로그 보관 경로 설정
        self.PATH.__setitem__("LOCAL_LOG", "{}/LocalLog/{}_LOG.txt".format(self.PATH.get("ROOT"), self.DATE_MARK))

        if not os.path.isdir("/".join(self.PATH.get("LOCAL_LOG").split("/")[:-1])):
            os.mkdir("/".join(self.PATH.get("LOCAL_LOG").split("/")[:-1]))

    @staticmethod
    def current_time():
        """
        현재 시간을 반환하는 메소드
        :return: 현재 날짜 + 시간
        """
        return datetime.datetime.now()

    def record_log(self, source_name, args):
        """
        Exception 을 기록하는 메소드
        :param source_name: 에러가 발생한 소스코드 네임
        :param args: sys.exc_info() // 발생된 Exception 정보
        :return: None
        """
        print(self.PATH)
        with open(self.PATH.get("LOCAL_LOG"), "a") as log:
            log.write("EXCEPTION OCCURRED TIME   : {}\n".format(self.current_time()))
            log.write("EXCEPTION OCCURRED SOURCE : {}\n".format(source_name))
            log.write("EXCEPTION CLASS           : {}\n".format(args[0]))
            log.write("EXCEPTION DESCRIPTION     : {}\n".format(args[1]))
            log.write("EXCEPTION OCCURRED LINE   : {}\n".format(args[2].tb_lineno))
            log.write("====================================================================================================\n")
