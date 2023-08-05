import pytest

from platone.exceptions import (
    BadFunctionCallOutput,
    NameNotFound,
)
from platone.utils.ens import (
    contract_ens_addresses,
    ens_addresses,
)


@pytest.fixture()
def math_addr(MathContract, address_conversion_func):
    web3 = MathContract.web3
    deploy_txn = MathContract.constructor().transact({'from': web3.platone.coinbase})
    deploy_receipt = web3.platone.waitForTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    return address_conversion_func(deploy_receipt['contractAddress'])


def test_contract_with_unset_address(MathContract):
    with contract_ens_addresses(MathContract, []):
        with pytest.raises(NameNotFound):
            MathContract(address='unsetname.eth')


def test_contract_with_name_address(MathContract, math_addr):
    with contract_ens_addresses(MathContract, [('thedao.eth', math_addr)]):
        mc = MathContract(address='thedao.eth')
        caller = mc.web3.platone.coinbase
        assert mc.address == 'thedao.eth'
        assert mc.functions.return13().call({'from': caller}) == 13


def test_contract_with_name_address_from_eth_contract(
    web3,
    MATH_ABI,
    MATH_CODE,
    MATH_RUNTIME,
    math_addr,
):
    with ens_addresses(web3, [('thedao.eth', math_addr)]):
        mc = web3.platone.contract(
            address='thedao.eth',
            abi=MATH_ABI,
            bytecode=MATH_CODE,
            bytecode_runtime=MATH_RUNTIME,
        )

        caller = mc.web3.platone.coinbase
        assert mc.address == 'thedao.eth'
        assert mc.functions.return13().call({'from': caller}) == 13


def test_contract_with_name_address_changing(MathContract, math_addr):
    # Contract address is validated once on creation
    with contract_ens_addresses(MathContract, [('thedao.eth', math_addr)]):
        mc = MathContract(address='thedao.eth')

    caller = mc.web3.platone.coinbase
    assert mc.address == 'thedao.eth'

    # what happen when name returns no address at all
    with contract_ens_addresses(mc, []):
        with pytest.raises(NameNotFound):
            mc.functions.return13().call({'from': caller})

    # what happen when name returns address to different contract
    with contract_ens_addresses(mc, [('thedao.eth', '0x' + '11' * 20)]):
        with pytest.raises(BadFunctionCallOutput):
            mc.functions.return13().call({'from': caller})

    # contract works again when name resolves correctly
    with contract_ens_addresses(mc, [('thedao.eth', math_addr)]):
        assert mc.functions.return13().call({'from': caller}) == 13
