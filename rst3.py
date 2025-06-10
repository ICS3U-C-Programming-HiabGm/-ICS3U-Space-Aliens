import ugame 
import stage 

#main function for game_scene
def game_scene():
    
    #image banks for circuit python 
    
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    #set the background to image 0 in the image bank
    background = stage.Grid(image_bank_background, 10, 8)
    
    # for a sprite that will update every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)
    
    #create a stage 
    game = stage.Stage(ugame.display, 60)
   
   #set layers of all sprites
    game.layers = [ship] + [background]
    
    game.render_block()
    
    
    
    while True:
        pass
    
if __name__ == "__main__":
    game_scene()
        
    