
import sys
from direct.showbase.ShowBase import ShowBase


class Application(ShowBase):

    def __init__(self):
        sys.path.insert(0, "../render_pipeline")
        sys.path.insert(0, "../render_pipeline/RenderPipeline")

        # Import the main render pipeline class
        from rpcore import RenderPipeline

        # Construct and create the pipeline
        self.render_pipeline = RenderPipeline()
        self.render_pipeline.create(self)

        # Done! You can start setting up your application stuff as regular now.


Application().run()
