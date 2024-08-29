import pytest
import allure
from operation.user import get_rank
from testcases.conftest import rank_data
from common.logger import logger


@allure.step("步骤1 ==>> 根据用户名来删除用户信息")
def step_1(username):
    logger.info("步骤1 ==>> 删除用户：{}".format(username))


@allure.step("前置登录步骤 ==>> 管理员登录")
def step_login(admin_user, token):
    logger.info("前置登录步骤 ==>> 管理员 {} 登录 ==>> 返回的 token 为：{}".format(admin_user, token))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户删除模块")
class TestUserRank():



    # @allure.story("用例--登录用户")
    # @allure.description("该用例是针对获取用户登录接口的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    # @allure.title("测试数据：【 {username}，{password}，{except_result}，{except_code}，{except_msg}】")
    # @pytest.mark.single
    @pytest.mark.parametrize("activityId, time, except_code, except_msg",
                             rank_data["test_get_rank_info"])
    def test_get_rank(self, activityId, time, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        logger.info(f"传入的参数为：activityId = {activityId}, time = {time}")
        # activityId="smg24_wzry"
        # time="1720666800000"
        result = get_rank(activityId,time)
        step_1("jasen")
        logger.info(f"测试用例层返回的结果信息{result}")
        # assert result.success == except_result, result.error
        # assert result.response.status_code == 200
        # assert result.success == except_result, result.error
        # logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        # assert result.response.json().get("code") == except_code
        # assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")

    # def test_login_user(self, activityId, time, except_result, except_code, except_msg):
    #     logger.info("*************** 开始执行用例 ***************")
    #     result = login_user(username, password)
    #     step_1(username)
    #     assert result.success == except_result, result.error
    #     assert result.response.status_code == 200
    #     assert result.success == except_result, result.error
    #     logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
    #     assert result.response.json().get("code") == except_code
    #     assert except_msg in result.msg
    #     logger.info("*************** 结束执行用例 ***************")




if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_06_rank.py"])
