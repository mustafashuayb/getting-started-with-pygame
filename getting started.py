# # # ## How to initialize all the imported modules in Pygame?
# # # # importing the library
# # # import pygame

# # # # initializing all the imported
# # # # pygame modules
# # # (numpass,numfail) = pygame.init()

# # # # printing the number of modules 
# # # # initialized successfully
# # # print('Number of modules initialized successfully:',
# # #       numpass)

# # # # importing the library
# # # import pygame

# # # # initializing the modules
# # # pygame.init()

# # # # checking the initialization
# # # is_initialized = pygame.get_init()

# # # # printing the result
# # # print('Is pygame modules initialized:',
# # #       is_initialized)

# # # ## How to create an empty Pygame window?
# # # # import pygame package
# # # import pygame

# # # # initializing imported module
# # # pygame.init()

# # # # displaying a window of height
# # # # 500 and width 400
# # # pygame.display.set_mode((400, 500))

# # # # creating a bool value which checks
# # # # if game is running
# # # running = True

# # # # keep game running till running is true
# # # while running:
    
# # #     # Check for event if user has pushed
# # #     # any event in queue
# # #     for event in pygame.event.get():
        
# # #         # if event is of type quit then 
# # #         # set running bool to false
# # #         if event.type == pygame.QUIT:
# # #             running = False

# # # ## How to get the size of Pygame window?
# # # # import package pygame
# # # import pygame

# # # # initialize pygame
# # # pygame.init()

# # # # Form screen
# # # screen = pygame.display.set_mode((500, 500))

# # # # get the size
# # # x, y = screen.get_size()

# # # # quit pygame
# # # pygame.display.quit()

# # # # view size (width x height)
# # # print(x, y)

# # # ## Allowing resizing window in PyGame
# # # # import package pygame
# # # import pygame

# # # # Form screen with 400x400 size
# # # # with not resizable
# # # screen = pygame.display.set_mode((400, 400))

# # # # set title
# # # pygame.display.set_caption('Not resizable')

# # # # run window
# # # running = True
# # # while running:
# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             running = False

# # # # quit pygame after closing window
# # # pygame.quit()

# # # ## How to change screen background color in Pygame?
# # # # Importing the library
# # # import pygame

# # # # Initializing Pygame modules
# # # pygame.init()

# # # # Initializing surface
# # # surface = pygame.display.set_mode((400, 300))

# # # # Initializing RGB Color
# # # color = (0, 0, 255)

# # # # Changing surface color
# # # surface.fill(color)
# # # pygame.display.flip()

# # # # How to Change the name of a Pygame window?
# # # # import pygame module
# # # import pygame

# # # # initializing imported module
# # # pygame.init()

# # # # Displaying a window of height 
# # # # 500 and width 400
# # # pygame.display.set_mode((400, 500))

# # # # Here we set name or title of our
# # # # pygame window
# # # pygame.display.set_caption('GeeksforGeeks')

# # # # Here we load the image we want to 
# # # # use
# # # Icon = pygame.image.load('gfglogo.png')

# # # # We use set_icon to set new icon
# # # pygame.display.set_icon(Icon)

# # # Creating a bool value which checks if 
# # # game is running
# # # running = True

# # # # Keep game running till running is true
# # # while running:
    
# # #     # Check for event if user has pushed 
# # #     # any event in queue
# # #     for event in pygame.event.get():
        
# # #         # If event is of type quit then set 
# # #         # running bool to false
# # #         if event.type == pygame.QUIT:
# # #             running = False

# # ## How to set up the game loop in pygame?

# # # # import pygame package
# # # import pygame

# # # # initializing imported module
# # # pygame.init()

# # # # displaying a window of height
# # # # 500 and width 400
# # # pygame.display.set_mode((400, 500))

# # # # Setting name for window
# # # pygame.display.set_caption('GeeksforGeeks')

# # # # creating a bool value which checks 
# # # # if game is running
# # # running = True

# # # # Game loop
# # # # keep game running till running is true
# # # while running:
  
# # #     # Check for event if user has pushed 
# # #     # any event in queue
# # #     for event in pygame.event.get():
      
# # #         # if event is of type quit then set
# # #         # running bool to false
# # #         if event.type == pygame.QUIT:
# # #             running = False

# # ## How to change the PyGame icon?
# # # Python program to change 
# # # the Pygame icon

# # # Import the library Pygame
# # import pygame

# # # Construct the GUI game
# # pygame.init()

# # # Set dimensions of game GUI
# # screen = pygame.display.set_mode([600, 400])

# # # Take image as input
# # img = pygame.image.load('gfg_image.jpg')

# # # Set image as icon
# # pygame.display.set_icon(img)

# # # Set running value
# # running = True

# # # Setting what happens when game 
# # # is in running state
# # while running:
# #     for event in pygame.event.get():

# #         # Close if the user quits the game
# #         if event.type == pygame.QUIT:
# #             running = False

# #     # Set the background color
# #     screen.fill((255, 255, 0))

# #     # Draw a circle on the screen
# #     pygame.draw.circle(screen, (0, 0, 0), (300, 200), 75)

# #     # Update the GUI game
# #     pygame.display.update()

# # # Quit the GUI game
# # pygame.quit()

# ## Python -Surfaces
# # Importing the library
# import pygame
# import time
  
# # Initializing Pygame
# pygame.init()
  
# # Creating the surface
# sample_surface = pygame.display.set_mode((400,300))
  
# # Choosing red color for the rectangle
# color = (255,255,0)
  
# # Drawing Rectangle
# pygame.draw.rect(sample_surface, color, 
#                  pygame.Rect(30, 30, 60, 60))

# # The pygame.display.flip() method is used 
# # to update content on the display screen
# pygame.display.flip()

## Python - Time
# # importing pygame module
# import pygame

# # importing sys module
# import sys

# # initialising pygame
# pygame.init()

# # creating display
# display = pygame.display.set_mode((500, 500))

# # Creating the image surface
# image = pygame.image.load('gfg_logo.png')

# # putting our image surface on display surface
# display.blit(image,(100,100))

# # making the script wait for 5000 milliseconds
# pygame.time.wait(5000)

# # creating a running loop
# while True:
  
#       # creating a loop to check events that are occurring
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     # updating the display
#     pygame.display.flip()

## Drawing Shapes
# # Pygame - Drawing Objects and Shapes
# # Importing pygame module
# import pygame
# from pygame.locals import *

# # initiate pygame and give permission
# # to use pygame's functionality.
# pygame.init()

# # create the display surface object
# # of specific dimension.
# window = pygame.display.set_mode((600, 600))

# # Fill the scree with white color
# window.fill((255, 255, 255))

# # Using draw.rect module of
# # pygame to draw the outlined rectangle
# pygame.draw.rect(window, (0, 0, 255), 
#                  [100, 100, 400, 100], 2)

# # Draws the surface object to the screen.
# pygame.display.update()

## Drawing different shapes on Pygame window
# # import pygame module in this program
# import pygame

# # activate the pygame library .
# # initiate pygame and give permission
# # to use pygame's functionality.
# pygame.init()

# # define the RGB value
# # for white, green,
# # blue, black, red
# # colour respectively.
# white = (255, 255, 255)
# green = (0, 255, 0)
# blue = (0, 0, 128)
# black = (0, 0, 0)
# red = (255, 0, 0)

# # assigning values to X and Y variable
# X = 400
# Y = 400

# # create the display surface object
# # of specific dimension..e(X,Y).
# display_surface = pygame.display.set_mode((X, Y ))

# # set the pygame window name
# pygame.display.set_caption('Drawing')

# # completely fill the surface object 
# # with white colour 
# display_surface.fill(white)

# # draw a polygon using draw.polygon()
# # method of pygame.
# # pygame.draw.polygon(surface, color, pointlist, thickness)
# # thickness of line parameter is optional.
# pygame.draw.polygon(display_surface, blue,
#                     [(146, 0), (291, 106),
#                     (236, 277), (56, 277), (0, 106)])
                    
# # draw a line using draw.line()
# # method of pygame.
# # pygame.draw.line(surface, color,
# # start point, end point, thickness) 
# pygame.draw.line(display_surface, green,
#                 (60, 300), (120, 300), 4)

# # draw a circle using draw.circle()
# # method of pygame.
# # pygame.draw.circle(surface, color,
# # center point, radius, thickness) 
# pygame.draw.circle(display_surface,
#            green, (300, 50), 20, 0)

# # draw a ellipse using draw.ellipse()
# # method of pygame.
# # pygame.draw.ellipse(surface, color,
# # bounding rectangle, thickness) 
# pygame.draw.ellipse(display_surface, black,
#                     (300, 250, 40, 80), 1)

# # draw a rectangle using draw.rect()
# # method of pygame.
# # pygame.draw.rect(surface, color,
# # rectangle tuple, thickness)
# # thickness of line parameter is optional.
# pygame.draw.rect(display_surface, black,
#                     (150, 300, 100, 50))

# # infinite loop
# while True :
    
#     # iterate over the list of Event objects
#     # that was returned by pygame.event.get() method.
#     for event in pygame.event.get() :

#         # if event object type is QUIT
#         # then quitting the pygame
#         # and program both.
#         if event.type == pygame.QUIT :

#             # deactivates the pygame library
#             pygame.quit()

#             # quit the program.
#             quit()

#         # Draws the surface object to the screen. 
#         pygame.display.update()

# How to draw rectangle in Pygame?
# import pygame
# pygame.init()  
# surface = pygame.display.set_mode((400, 300))  # window
# color = (255, 192, 203)  

# pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))  
# pygame.display.flip() 
# pygame.time.wait(3000)  # Pause for 3 seconds
# pygame.quit()
## How to draw a rectangle with rounded corner in PyGame?
# # Importing the library
# import pygame

# # Initializing Pygame
# pygame.init()

# # Initializing surface
# surface = pygame.display.set_mode((400, 300))

# # Initializing Color
# color = (48, 141, 70)

# # Drawing Rectangle
# pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60),  2, 3)
# pygame.display.flip()