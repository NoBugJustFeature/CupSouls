import arcade
import arcade.gui as gui


class ScoreView(arcade.View):
    def __init__(self, 
                width: int = 800, 
                height: int = 600):
        super().__init__()

        self.width = width
        self.height = height

        self.background = arcade.load_texture("sprites/background/Forest/Image without mist.png")

        self.setup()


    def setup(self):
        """
        Activate UI manager
        """
        self.manager = gui.UIManager()
        self.manager.enable()

        """
        Create group of buttons (vertical grid)
        """
        self.v_box = gui.UIBoxLayout()

        """
        Create buttons
        """
        back_button = gui.UIFlatButton(text="Назад",
                                               width=300)
        
        """
        Create labels
        """
        scores_label = gui.UITextArea(text=self.get_scores(), 
                                      height = 300,
                                      text_color=(255, 0, 0, 255), 
                                      font_size=20)
        
        """
        Add buttons in the group
        """
        self.v_box.add(scores_label.with_space_around(bottom=20))
        self.v_box.add(back_button.with_space_around(bottom=20))


        """
        Add on-click evenst
        """
        @back_button.event("on_click")
        def om_click_quit(event):
            from views.start_view import StartView
            start_view = StartView(self.width,
                                self.height)
            
            self.window.show_view(start_view)

        """
        Create vidget
        """
        self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box
                )
        )

        
    def on_draw(self):
        arcade.draw_texture_rectangle(self.width/2, 
                                      self.height/2, 
                                      width=self.width, 
                                      height=self.height, 
                                      texture=self.background)
        self.manager.draw()


    def get_scores(self) -> str:
            with open("score.txt", mode="r") as f:
                return "\n".join(f.readlines())
