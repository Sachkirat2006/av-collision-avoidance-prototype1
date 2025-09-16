from decision import decide_action

def test_decision_logic():
    assert decide_action(15) == "SAFE"
    assert decide_action(8) in ["STEER!", "BRAKE!"]  # close hazard
    assert decide_action(3) == "BRAKE!"
