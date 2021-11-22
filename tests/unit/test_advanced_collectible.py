from brownie import network, AdvancedCollectible
import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_contract, get_account
from scripts.advanced_collectible.deploy_and_create import deploy_and_create

def test_can_create_advanced_collectible():
    # deploy the contract
    # create and NFT
    # get a random breed back
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local test")
    account = get_account()
    advanced_collectible, creation_tx = deploy_and_create()
    request_id = creation_tx.events["requestedCollectible"]["requestId"]
    randomNumber = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        request_id, randomNumber, advanced_collectible.address, {"from": account}
    )
    assert advanced_collectible.tokenCounter() > 0
    assert advanced_collectible.tokenIdToBreed(0) == randomNumber % 3
