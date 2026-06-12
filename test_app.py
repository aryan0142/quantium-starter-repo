from app_improved import app

def test_header_present():
    layout_str = str(app.layout)
    assert "Soul Foods Pink Morsel Sales Dashboard" in layout_str

def test_graph_present():
    layout_str = str(app.layout)
    assert "sales-chart" in layout_str

def test_region_picker_present():
    layout_str = str(app.layout)
    assert "region-filter" in layout_str