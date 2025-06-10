import ugame

import stage



import constants



def game_scene():

    #this function is the main game scene





    #image banks for circuitPython

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")





    # set the background to image 0 in the image bank

    #  and the size (10x8 titles of size 16x16)

    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)



    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants. SPRITE_SIZE))



    #create a stage for the background to show up on

    #  and set the frame rate to 60fps

    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers, items show up in folder

    game.layers = [ship] + [background]

    # render the background and initial location of sprite list

    # most likely you will only render background once per scene

    game.render_block()





    while True:

        # get user input

        keys = ugame.buttons.get_pressed()





        if keys & ugame.K_X:

            pass

        if keys & ugame.K_O:

            pass

        if keys & ugame.K_START:

            pass

        if keys & ugame.K_SELECT:

            pass

        if keys & ugame.K_RIGHT:

            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:

                ship.move(ship.x + 1, ship.y)

            else:

                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)

               

        if keys & ugame.K_LEFT:

            if ship.x >= 0:

                ship.move(ship.x - 1, ship.y)

            else:

                ship.move(0, ship.y)

               

        if keys & ugame.K_UP:

            if ship.y <= constants.SCREEN_Y - constants.SPRITE_SIZE:

                ship.move(ship.x, ship.y - 1)

            else:

                ship.move(ship.x ,constants.SCREEN_Y - constants.SPRITE_SIZE)

        if keys & ugame.K_DOWN:

            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:

                ship.move(ship.x, ship.y + 1)

            else:

                ship.move(ship.x ,constants.SCREEN_X - constants.SPRITE_SIZE)



        # update game Logic



        #update game logic



        # redraw sprites

        game.render_block()

        game.render_sprites([ship])

        game.tick()

   

if __name__ == "__main__":

    game_scene()

   

