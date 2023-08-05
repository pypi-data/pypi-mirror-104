
import json
import pytest

from eth_tester import (
    EthereumTester,
)

from platone.packages.ens  import ENS
from platone.packages.ens .contract_data import (
    registrar_abi,
    registrar_bytecode,
    registrar_bytecode_runtime,
    resolver_abi,
    resolver_bytecode,
    resolver_bytecode_runtime,
    reverse_registrar_abi,
    reverse_registrar_bytecode,
    reverse_registrar_bytecode_runtime,
    reverse_resolver_abi,
    reverse_resolver_bytecode,
    reverse_resolver_bytecode_runtime,
)
from platone import Web3
from platone.contract import (
    Contract,
)
from platone.providers.eth_tester import (
    EthereumTesterProvider,
)


def bytes32(val):
    if isinstance(val, int):
        result = Web3.toBytes(val)
    else:
        raise TypeError('val %r could not be converted to bytes')
    if len(result) < 32:
        return result.rjust(32, b'\0')
    else:
        return result


def deploy(w3, Factory, from_address, args=None):
    args = args or []
    factory = Factory(w3)
    deploy_txn = factory.constructor(*args).transact({'from': from_address})
    deploy_receipt = w3.platone.waitForTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    return factory(address=deploy_receipt['contractAddress'])


def DefaultReverseResolver(w3):
    return w3.platone.contract(
        bytecode=reverse_resolver_bytecode,
        bytecode_runtime=reverse_resolver_bytecode_runtime,
        abi=reverse_resolver_abi,
        ContractFactoryClass=Contract,
    )


def ReverseRegistrar(w3):
    return w3.platone.contract(
        bytecode=reverse_registrar_bytecode,
        bytecode_runtime=reverse_registrar_bytecode_runtime,
        abi=reverse_registrar_abi,
        ContractFactoryClass=Contract,
    )


def PublicResolverFactory(w3):
    return w3.platone.contract(
        bytecode=resolver_bytecode,
        bytecode_runtime=resolver_bytecode_runtime,
        abi=resolver_abi,
        ContractFactoryClass=Contract,
    )


def ENSFactory(w3):
    return w3.platone.contract(
        bytecode="6060604052341561000f57600080fd5b60008080526020527fad3228b676f7d3cd4284a5443f17f1962b36e491b30a40b2405849e597ba5fb58054600160a060020a033316600160a060020a0319909116179055610501806100626000396000f300606060405236156100805763ffffffff7c01000000000000000000000000000000000000000000000000000000006000350416630178b8bf811461008557806302571be3146100b757806306ab5923146100cd57806314ab9038146100f457806316a25cbd146101175780631896f70a1461014a5780635b0fc9c31461016c575b600080fd5b341561009057600080fd5b61009b60043561018e565b604051600160a060020a03909116815260200160405180910390f35b34156100c257600080fd5b61009b6004356101ac565b34156100d857600080fd5b6100f2600435602435600160a060020a03604435166101c7565b005b34156100ff57600080fd5b6100f260043567ffffffffffffffff60243516610289565b341561012257600080fd5b61012d600435610355565b60405167ffffffffffffffff909116815260200160405180910390f35b341561015557600080fd5b6100f2600435600160a060020a036024351661038c565b341561017757600080fd5b6100f2600435600160a060020a0360243516610432565b600090815260208190526040902060010154600160a060020a031690565b600090815260208190526040902054600160a060020a031690565b600083815260208190526040812054849033600160a060020a039081169116146101f057600080fd5b8484604051918252602082015260409081019051908190039020915083857fce0457fe73731f824cc272376169235128c118b49d344817417c6d108d155e8285604051600160a060020a03909116815260200160405180910390a3506000908152602081905260409020805473ffffffffffffffffffffffffffffffffffffffff1916600160a060020a03929092169190911790555050565b600082815260208190526040902054829033600160a060020a039081169116146102b257600080fd5b827f1d4f9bbfc9cab89d66e1a1562f2233ccbf1308cb4f63de2ead5787adddb8fa688360405167ffffffffffffffff909116815260200160405180910390a250600091825260208290526040909120600101805467ffffffffffffffff90921674010000000000000000000000000000000000000000027fffffffff0000000000000000ffffffffffffffffffffffffffffffffffffffff909216919091179055565b60009081526020819052604090206001015474010000000000000000000000000000000000000000900467ffffffffffffffff1690565b600082815260208190526040902054829033600160a060020a039081169116146103b557600080fd5b827f335721b01866dc23fbee8b6b2c7b1e14d6f05c28cd35a2c934239f94095602a083604051600160a060020a03909116815260200160405180910390a250600091825260208290526040909120600101805473ffffffffffffffffffffffffffffffffffffffff1916600160a060020a03909216919091179055565b600082815260208190526040902054829033600160a060020a0390811691161461045b57600080fd5b827fd4735d920b0f87494915f556dd9b54c8f309026070caea5c737245152564d26683604051600160a060020a03909116815260200160405180910390a250600091825260208290526040909120805473ffffffffffffffffffffffffffffffffffffffff1916600160a060020a039092169190911790555600a165627a7a7230582050975b6c54a16d216b563f4c4960d6ebc5881eb1ec73c2ef1f87920a251159530029",  # noqa: E501
        bytecode_runtime="606060405236156100805763ffffffff7c01000000000000000000000000000000000000000000000000000000006000350416630178b8bf811461008557806302571be3146100b757806306ab5923146100cd57806314ab9038146100f457806316a25cbd146101175780631896f70a1461014a5780635b0fc9c31461016c575b600080fd5b341561009057600080fd5b61009b60043561018e565b604051600160a060020a03909116815260200160405180910390f35b34156100c257600080fd5b61009b6004356101ac565b34156100d857600080fd5b6100f2600435602435600160a060020a03604435166101c7565b005b34156100ff57600080fd5b6100f260043567ffffffffffffffff60243516610289565b341561012257600080fd5b61012d600435610355565b60405167ffffffffffffffff909116815260200160405180910390f35b341561015557600080fd5b6100f2600435600160a060020a036024351661038c565b341561017757600080fd5b6100f2600435600160a060020a0360243516610432565b600090815260208190526040902060010154600160a060020a031690565b600090815260208190526040902054600160a060020a031690565b600083815260208190526040812054849033600160a060020a039081169116146101f057600080fd5b8484604051918252602082015260409081019051908190039020915083857fce0457fe73731f824cc272376169235128c118b49d344817417c6d108d155e8285604051600160a060020a03909116815260200160405180910390a3506000908152602081905260409020805473ffffffffffffffffffffffffffffffffffffffff1916600160a060020a03929092169190911790555050565b600082815260208190526040902054829033600160a060020a039081169116146102b257600080fd5b827f1d4f9bbfc9cab89d66e1a1562f2233ccbf1308cb4f63de2ead5787adddb8fa688360405167ffffffffffffffff909116815260200160405180910390a250600091825260208290526040909120600101805467ffffffffffffffff90921674010000000000000000000000000000000000000000027fffffffff0000000000000000ffffffffffffffffffffffffffffffffffffffff909216919091179055565b60009081526020819052604090206001015474010000000000000000000000000000000000000000900467ffffffffffffffff1690565b600082815260208190526040902054829033600160a060020a039081169116146103b557600080fd5b827f335721b01866dc23fbee8b6b2c7b1e14d6f05c28cd35a2c934239f94095602a083604051600160a060020a03909116815260200160405180910390a250600091825260208290526040909120600101805473ffffffffffffffffffffffffffffffffffffffff1916600160a060020a03909216919091179055565b600082815260208190526040902054829033600160a060020a0390811691161461045b57600080fd5b827fd4735d920b0f87494915f556dd9b54c8f309026070caea5c737245152564d26683604051600160a060020a03909116815260200160405180910390a250600091825260208290526040909120805473ffffffffffffffffffffffffffffffffffffffff1916600160a060020a039092169190911790555600a165627a7a7230582050975b6c54a16d216b563f4c4960d6ebc5881eb1ec73c2ef1f87920a251159530029",  # noqa: E501
        abi=json.loads('[{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"resolver","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"label","type":"bytes32"},{"name":"owner","type":"address"}],"name":"setSubnodeOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"ttl","type":"uint64"}],"name":"setTTL","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"ttl","outputs":[{"name":"","type":"uint64"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"resolver","type":"address"}],"name":"setResolver","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"owner","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":true,"name":"label","type":"bytes32"},{"indexed":false,"name":"owner","type":"address"}],"name":"NewOwner","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"owner","type":"address"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"resolver","type":"address"}],"name":"NewResolver","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"ttl","type":"uint64"}],"name":"NewTTL","type":"event"}]'),  # noqa: E501
        ContractFactoryClass=Contract,
    )


def ETHRegistrarFactory(w3):
    return w3.platone.contract(
        bytecode=registrar_bytecode,
        bytecode_runtime=registrar_bytecode_runtime,
        abi=registrar_abi,
        ContractFactoryClass=Contract,
    )


# session scope for performance
@pytest.fixture(scope="session")
def ens_setup():
    w3 = Web3(EthereumTesterProvider(EthereumTester()))

    # ** Set up ENS contracts **

    # remove account that creates ENS, so test transactions don't have write access
    accounts = w3.platone.accounts
    ens_key = accounts.pop()

    # create ENS contract
    eth_labelhash = w3.sha3(text='eth')
    eth_namehash = bytes32(0x93cdeb708b7545dc668eb9280176169d1c33cfd8ed6f04690a0bcc88a93fc4ae)
    resolver_namehash = bytes32(0xfdd5d5de6dd63db72bbc2d487944ba13bf775b50a80805fe6fcaba9b0fba88f5)
    reverse_tld_namehash = bytes32(0xa097f6721ce401e757d1223a763fef49b8b5f90bb18567ddb86fd205dff71d34)  # noqa: E501
    reverser_namehash = bytes32(0x91d1777781884d03a6757a803996e38de2a42967fb37eeaca72729271025a9e2)
    ens_contract = deploy(w3, ENSFactory, ens_key)

    # create public resolver
    public_resolver = deploy(w3, PublicResolverFactory, ens_key, args=[ens_contract.address])

    # set 'resolver.eth' to resolve to public resolver
    ens_contract.functions.setSubnodeOwner(
        b'\0' * 32,
        eth_labelhash,
        ens_key
    ).transact({'from': ens_key})

    ens_contract.functions.setSubnodeOwner(
        eth_namehash,
        w3.sha3(text='resolver'),
        ens_key
    ).transact({'from': ens_key})

    ens_contract.functions.setResolver(
        resolver_namehash,
        public_resolver.address
    ).transact({'from': ens_key})

    public_resolver.functions.setAddr(
        resolver_namehash,
        public_resolver.address
    ).transact({'from': ens_key})

    # create .eth auction registrar
    eth_registrar = deploy(
        w3,
        ETHRegistrarFactory,
        ens_key,
        args=[ens_contract.address, eth_namehash, 1],
    )

    # set '.eth' to resolve to the registrar
    ens_contract.functions.setResolver(
        eth_namehash,
        public_resolver.address
    ).transact({'from': ens_key})

    public_resolver.functions.setAddr(
        eth_namehash,
        eth_registrar.address
    ).transact({'from': ens_key})

    # create reverse resolver
    reverse_resolver = deploy(w3, DefaultReverseResolver, ens_key, args=[ens_contract.address])

    # create reverse registrar
    reverse_registrar = deploy(
        w3,
        ReverseRegistrar,
        ens_key,
        args=[ens_contract.address, reverse_resolver.address]
    )

    # set 'addr.reverse' to resolve to reverse registrar
    ens_contract.functions.setSubnodeOwner(
        b'\0' * 32,
        w3.sha3(text='reverse'),
        ens_key
    ).transact({'from': ens_key})

    ens_contract.functions.setSubnodeOwner(
        reverse_tld_namehash,
        w3.sha3(text='addr'),
        ens_key
    ).transact({'from': ens_key})

    ens_contract.functions.setResolver(
        reverser_namehash,
        public_resolver.address
    ).transact({'from': ens_key})

    public_resolver.functions.setAddr(
        reverser_namehash,
        reverse_registrar.address
    ).transact({'from': ens_key})

    # set owner of tester.eth to an account controlled by tests
    ens_contract.functions.setSubnodeOwner(
        eth_namehash,
        w3.sha3(text='tester'),
        w3.platone.accounts[2]  # note that this does not have to be the default, only in the list
    ).transact({'from': ens_key})

    # make the registrar the owner of the 'eth' name
    ens_contract.functions.setSubnodeOwner(
        b'\0' * 32,
        eth_labelhash,
        eth_registrar.address
    ).transact({'from': ens_key})

    # make the reverse registrar the owner of the 'addr.reverse' name
    ens_contract.functions.setSubnodeOwner(
        reverse_tld_namehash,
        w3.sha3(text='addr'),
        reverse_registrar.address
    ).transact({'from': ens_key})

    return ENS.fromWeb3(w3, ens_contract.address)


@pytest.fixture
def ens(ens_setup, mocker):
    mocker.patch('web3.middleware.stalecheck._isfresh', return_value=True)
    ens_setup.web3.platone.defaultAccount = ens_setup.web3.platone.coinbase
    return ens_setup


@pytest.fixture()
def TEST_ADDRESS(address_conversion_func):
    return address_conversion_func("0x000000000000000000000000000000000000dEaD")
