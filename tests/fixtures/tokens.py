import boa
import pytest


@pytest.fixture(scope="module")
def weth(deployer):
    with boa.env.prank(deployer):
        return boa.load("contracts/mocks/WETH.vy")


@pytest.fixture(scope="module")
def usd(deployer):
    with boa.env.prank(deployer):
        return boa.load("contracts/mocks/ERC20Mock.vy", "USD", "USD", 18)


@pytest.fixture(scope="module")
def btc(deployer):
    with boa.env.prank(deployer):
        return boa.load("contracts/mocks/ERC20Mock.vy", "BTC", "BTC", 18)


@pytest.fixture(scope="module")
def stg(deployer):
    with boa.env.prank(deployer):
        return boa.load("contracts/mocks/ERC20Mock.vy", "STG", "STG", 18)


@pytest.fixture(scope="module")
def usdt(deployer):
    with boa.env.prank(deployer):
        return boa.load("contracts/mocks/ERC20Mock.vy", "USDT", "USDT", 6)


@pytest.fixture(scope="module")
def usdc(deployer):
    with boa.env.prank(deployer):
        return boa.load("contracts/mocks/ERC20Mock.vy", "USDC", "USDC", 6)


@pytest.fixture(scope="module")
def dai(deployer):
    with boa.env.prank(deployer):
        return boa.load("contracts/mocks/ERC20Mock.vy", "DAI", "DAI", 18)


@pytest.fixture(scope="module")
def coins(usd, weth):
    yield [usd, weth]


@pytest.fixture(scope="module")
def stgusdc(usdt, weth):
    yield [stg, usdc]


@pytest.fixture(scope="module")
def stablecoins(usdc, usdt, dai):
    yield [dai, usdc, usdt]


@pytest.fixture(scope="module")
def pool_coins(coins):
    yield coins
