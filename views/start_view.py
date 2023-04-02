import arcade
import arcade.gui

from views.game_view import GameView

class StartView(arcade.View):
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
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        """
        Create group of buttons (vertical grid)
        """
        self.v_box = arcade.gui.UIBoxLayout()

        """
        Create the buttons
        """
        start_button = arcade.gui.UIFlatButton(text="Играть",
                                               width=200)
        results_button = arcade.gui.UIFlatButton(text="Результаты",
                                               width=200)
        quit_button = arcade.gui.UIFlatButton(text="Выход",
                                               width=200)
        
        """
        Add buttons in the group
        """
        self.v_box.add(start_button.with_space_around(bottom=20))
        self.v_box.add(results_button.with_space_around(bottom=20))
        self.v_box.add(quit_button.with_space_around(bottom=20))

        """
        Add on-click evenst
        """
        @start_button.event("on_click")
        def on_click_start(event):
            game_view = GameView(self.width,
                                self.height)
            
            self.window.show_view(game_view)

        @quit_button.event("on_click")
        def om_click_quit(event):
            arcade.exit()

        """
        Create vidget
        """
        self.manager.add(
            arcade.gui.UIAnchorWidget(
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