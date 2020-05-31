import cv2
import numpy as np
import math
import time

# import geometry

import engine

from .threaded_engine_controller import ThreadedEngineController

WINDOW_NAME = "DISPLAY"

TEXT_MARGIN = 10
TEXT_ROW_1 = 20
TEXT_ROW_2 = 40
TEXT_ROW_3 = 60
TEXT_ROW_4 = 80
TEXT_ROW_5 = 100
TEXT_ROW_6 = 120
TEXT_ROW_7 = 140
TEXT_ROW_8 = 160
TEXT_ROW_9 = 180


COLOUR_BLUE = (255, 0, 0)
COLOUR_GREEN = (0, 255, 0)
COLOUR_RED = (0, 0, 255)
COLOUR_YELLOW = (0, 255, 255)
COLOUR_WHITE = (255, 255, 255)


COLOUR_GOOD = COLOUR_GREEN
COLOUR_BAD = COLOUR_RED


class OpencvImageController(ThreadedEngineController):

    def __init__(self):
        super(OpencvImageController, self).__init__()

        cv2.namedWindow(WINDOW_NAME)

        self._image_to_show = None

    def notify_state_update(self, state, status_txt=""):
        super(OpencvImageController, self).notify_state_update(state, status_txt)

        if state == engine.ApplicationEngine.CONTROLLER_STATE_IDLE:
            print("opencv display init as blank")
            cv2.imshow(WINDOW_NAME, np.zeros((100, 100, 3), np.uint8))

    def notify_frame_data(self, frameData):
        texture_image = frameData.getTextureImage()
        if len(texture_image.shape) == 2:
            texture_image = cv2.cvtColor(texture_image, cv2.COLOR_GRAY2BGR)

        print("notify_frame_data")
        self._image_to_show = texture_image

    def run(self):
        print(self._engine_shutdown)
        while not self._engine_shutdown:

            if self._image_to_show is not None:
                cv2.imshow(WINDOW_NAME, self._image_to_show)
                self._image_to_show = None
                print("image is not none")
                k = cv2.waitKey(1)
                print(k)
            #
            # # Mask out all but the equivalent ASCII key code in the low byte
            # k = k & 0xFF
            # print(k)
            # if k == 32:  # SPACE
            #     if self._controller_state == engine.ApplicationEngine.CONTROLLER_STATE_IDLE:
            #         self.signal_start_capture()
            #     elif self._controller_state == engine.ApplicationEngine.CONTROLLER_STATE_RUNNING_CAPTURE:
            #         self.signal_complete_capture()
            # elif k == ord('t'):
            #     self.signal_trigger_down()
            # elif k == ord('y'):
            #     self.signal_trigger_up()
            # elif k == ord('q'):
            #     self.signal_shutdown()
            # elif k == ord('u'):
            #     self.signal_upload()

    def __del__(self):
        super(OpencvImageController, self).__del__()
        cv2.destroyAllWindows()
