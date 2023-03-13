# dummy converters throw warnings method encountered
import tensorrt as trt
from .dummy_converters import *

# supported converters will override dummy converters

from .AdaptiveAvgPool2d import *
from .BatchNorm1d import *
from .BatchNorm2d import *
from .BatchNorm3d import *
from .clone import *
from .conv_functional import *
from .Conv import *
from .Conv1d import *
from .Conv2d import *
from .ConvTranspose import *
from .ConvTranspose2d import *
from .Linear import *
from .LogSoftmax import *
from .activation import *
from .adaptive_avg_pool2d import *
from .adaptive_avg_pool3d import *
from .adaptive_max_pool2d import *
from .adaptive_max_pool3d import *
from .add import *
from .avg_pool import *
from .batch_norm import *
from .cat import *
from .chunk import *
from .clamp import *
from .compare import *
from .div import *
from .einsum import *
from .expand import *
from .example_plugin import *
from .flatten import *
from .floordiv import *
from .gelu import *
from .getitem import *
from .group_norm import *
from .identity import *
from .instance_norm import *
from .interpolate import *
from .layer_norm import *
from .matmul import *
from .max import *
from .max_pool1d import *
from .max_pool2d import *
from .max_pool3d import *
from .mean import *
from .min import *
from .mod import *
from .mul import *
from .normalize import *
from .ne import *
from .narrow import *
from .pad import *
from .permute import *
from .pow import *
from .prelu import *
from .prod import *
from .reflection_pad_2d import *
from .relu import *
from .relu6 import *
from .roll import *
from .sigmoid import *
from .silu import *
from .softmax import *
from .split import *
from .squeeze import *
from .stack import *
from .sub import *
from .sum import *
from .tanh import *
from .tensor import *
from .transpose import *
from .unary import *
from .unsqueeze import *
from .view import *