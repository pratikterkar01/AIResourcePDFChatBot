import time
class Timer:
  def __init__(self):
    self._start_time = None
    self._elapsed_time = None

  def start(self):
    if self._start_time is not None:
      raise Exception("Timer is running")
    self._start_time = time.perf_counter()

  def end(self):
    if self._start_time is None:
      raise ExceptionTimer("Timmer not start")
    self._elapsed_time = time.perf_counter() - self._start_time
    self._start_time = None


  def elapsed(self):
    if self._elapsed_time is None:
      raise ExceptionTimer("Timer have not been start yet, start timer")
    return self._elapsed_time

  def __str__(self):
    "print( the string)"
    return (str(self._elapsed_time))

  def show_elapsed_time(self):
      return  str(self._elapsed_time)