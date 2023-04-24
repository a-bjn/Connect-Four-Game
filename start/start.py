from repository.repository import GridRepository
from services.gridServices import GridService

from ui.ui import Ui

grid_repo = GridRepository()
grid_service = GridService(grid_repo)


ui = Ui(grid_service)
ui.start()
