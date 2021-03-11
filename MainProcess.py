from Modules.tokenizer import SchoolRuleTokenizer


if __name__ == '__main__':
    SRT = SchoolRuleTokenizer()

    print(SRT.tokenizer("제1조(목적) 본 대학은 대한민국 교육의 근본이념에 입각하여 열린 평생교육을 지향하며 국가산업 발전에 필요한 전문적인 지식을 연구.교수하고 재능을 연마하여 국가사회 발 전에 필요한 전문직업인을 양성하고, 전문지식을 활용하여 지역사회 발전에 기여함을 목적으로 한다."))
