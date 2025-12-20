

import logging
from pathlib import Path
from datetime import datetime


logger_name = 'perturbations'
log_dir = 'logs'


def get_logger(name=logger_name, log_dir=log_dir):

    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        Path(log_dir).mkdir(exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # log file
        file_handler = logging.FileHandler(f'{log_dir}/audio_{timestamp}.log')
        file_handler.setFormatter(
            logging.Formatter(
                '%(levelname)s - [%(filename)s:%(lineno)d - %(funcName)s] - %(message)s'
            )
        )
        
        # console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(
            logging.Formatter(
                '%(levelname)s - %(message)s'
            )
        )
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger


# # All available format variables:
# format = '%(asctime)s'      # 2025-10-11 14:30:22
# format = '%(levelname)s'    # INFO, WARNING, ERROR
# format = '%(name)s'         # Logger name ('audio')
# format = '%(filename)s'     # Script filename (main.py)
# format = '%(lineno)d'       # Line number (42)
# format = '%(funcName)s'     # Function name (analyze_file)
# format = '%(pathname)s'     # Full path (/home/user/project/main.py)
# format = '%(module)s'       # Module name (main)
# format = '%(message)s'      # Your actual message


def log_section(title, char='=', width=70):
  logger = get_logger()
  logger.info(char * width)
  logger.info(title.center(width))
  logger.info(char * width)

def log_file_start(filename):
  logger = get_logger()
  log_section(f"Processing: {filename}")
  logger.info(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def log_file_end(filename, success=True):
  logger = get_logger()
  status = "✓ SUCCESS" if success else "✗ FAILED"
  logger.info(f"{status}: {filename}")
  logger.info(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
  logger.info("=" * 70 + "\n")

def log_quality_metric(metric_name, value, threshold=None, unit=""):
  logger = get_logger()
  msg = f"{metric_name}: {value:.2f}{unit}"
  
  if threshold is not None:
      if value < threshold:
          logger.warning(f"{msg} (below threshold: {threshold}{unit})")
      else:
          logger.info(f"{msg} ✓")
  else:
      logger.info(msg)

def log_stats(stats_dict, title="Statistics"):
  logger = get_logger()
  logger.info(f"\n{title}:")
  for key, value in stats_dict.items():
      if isinstance(value, float):
          logger.info(f"  {key}: {value:.4f}")
      else:
          logger.info(f"  {key}: {value}")

def log_error_context(filename, error, context=""):
  logger = get_logger()
  logger.error(f"✗ ERROR in {filename}")
  if context:
      logger.error(f"Context: {context}")
  logger.error(f"Error: {str(error)}")
  logger.exception("Full traceback:")

def log_batch_summary(total, success, failed):
  logger = get_logger()
  log_section("BATCH PROCESSING COMPLETE")
  logger.info(f"Total files: {total}")
  logger.info(f"✓ Successful: {success}")
  logger.info(f"✗ Failed: {failed}")
  logger.info(f"Success rate: {success/total*100:.1f}%")