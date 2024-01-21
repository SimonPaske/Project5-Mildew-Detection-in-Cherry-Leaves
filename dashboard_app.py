from app_pages.multipage import MultiPage

# Load pages
from app_pages.summary import summary_page
from app_pages.project_hypothesis import project_hypothesis_page
from app_pages.leaf_visualizer import leaf_visualizer_page
from app_pages.model_performance import model_performance
from app_pages.detector import mildew_detector_page

app = MultiPage(app_name="Cherry Leaves Mildew Detector")


app.add_page("Project Summary", summary_page)
app.add_page("Project Hypothesis", project_hypothesis_page)
app.add_page("Leaf Visualizer", leaf_visualizer_page)
app.add_page("Model Performance", model_performance)
app.add_page("Mildew Detector", mildew_detector_page)


app.run()
