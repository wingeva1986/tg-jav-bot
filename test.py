# -*- coding: UTF-8 -*-
import jvav
import unittest

PROXY_ADDR = ''
#PROXY_ADDR = "http://127.0.0.1:7890"


def assert_code(code: int, res):
    """确认状态码是否为 200, 如果是则打印结果

    :param int code: 状态码
    :param any res: 结果
    """
    assert code == 200, f"code={code}"
    print(res)


def assert_res(res):
    assert res != None, f"res=None"
    print(res)



# python -m unittest discover -s tests -k JavBusUtilTest
class JavBusUtilTest(unittest.TestCase):
    util = jvav.JavBusUtil(
        proxy_addr=PROXY_ADDR, max_home_page_count=100, max_new_avs_count=10
    )

    def test_get_all_genres(self):
        assert_code(*JavBusUtilTest.util.get_all_genres())

    def test_get_id_by_genre_id(self):
        assert_code(*JavBusUtilTest.util.get_id_by_genre_id("3s"))

    # python -m unittest discover -s tests -k test_get_max_page
    def test_get_max_page(self):
        assert_code(
            *JavBusUtilTest.util.get_max_page("https://www.javbus.com/star/okq")
        )

    def test_get_ids_from_page(self):
        assert_code(
            *JavBusUtilTest.util.get_ids_from_page(
                base_page_url="https://www.javbus.com/star/okq"
            )
        )

    def test_get_id_from_page(self):
        assert_code(
            *JavBusUtilTest.util.get_id_from_page(
                base_page_url="https://www.javbus.com/star/okq"
            )
        )

    def test_get_id_from_home(self):
        assert_code(*JavBusUtilTest.util.get_id_from_home())

    def test_get_id_by_star_name(self):
        assert_code(*JavBusUtilTest.util.get_id_by_star_name(star_name="三上悠亜"))

    def test_get_new_ids_by_star_name(self):
        assert_code(*JavBusUtilTest.util.get_new_ids_by_star_name(star_name="三上悠亜"))

    def test_get_id_by_star_id(self):
        assert_code(*JavBusUtilTest.util.get_id_by_star_id(star_id="okq"))

    def test_get_new_ids_by_star_id(self):
        assert_code(*JavBusUtilTest.util.get_new_ids_by_star_id(star_id="okq"))

    def test_get_samples_by_id(self):
        assert_code(*JavBusUtilTest.util.get_samples_by_id(id="ipx-365"))

    def test_check_star_exists(self):
        assert_code(*JavBusUtilTest.util.check_star_exists(star_name="三上"))

    def test_get_av_by_id(self):
        assert_code(
            *JavBusUtilTest.util.get_av_by_id(
                id="ipx-365", is_nice=True, is_uncensored=False
            )
        )
        assert_code(
            *JavBusUtilTest.util.get_av_by_id(
                id="NINE-078", is_nice=True, is_uncensored=False
            )
        )




if __name__ == "__main__":
    unittest.main()
