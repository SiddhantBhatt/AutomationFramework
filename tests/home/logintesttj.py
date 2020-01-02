from test_junkie.runner import Runner
from tests.home.login_tests_usingtj import LoginTestsTJ

runner = Runner(suites=[LoginTestsTJ])
runner.run()

