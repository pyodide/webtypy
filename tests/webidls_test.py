from js_pyi.webidls import find, find_all


def x_test_webidls_presence():
    assert "interface Document" in find("Document.webidl").read_text()
    assert "interface Bluetooth" in find("Bluetooth.webidl").read_text()
    assert "interface PaymentRequest" in find("PaymentRequest.webidl").read_text()


def x_test_findall():
    actual = find_all()
    assert find("Document.webidl") in actual
    assert find("Bluetooth.webidl") in actual
    assert find("PaymentRequest.webidl") in actual
    assert find("FileMode.webidl") in actual
