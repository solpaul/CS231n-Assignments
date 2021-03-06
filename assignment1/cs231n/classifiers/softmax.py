import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  
  num_classes = W.shape[1]
  num_train = X.shape[0]

  for i in xrange(num_train):
    scores = X[i].dot(W)    
    scores -= np.max(scores)
    correct_class_score = scores[y[i]]
    
    loss += -np.log(np.exp(correct_class_score) / np.sum(np.exp(scores)))
    
    for j in xrange(num_classes):
      if j == y[i]:
        dW[:, j] += X[i] * ((np.exp(scores[j]) / np.sum(np.exp(scores))) - 1)
        continue
      dW[:, j] += X[i] * np.exp(scores[j]) / np.sum(np.exp(scores))
    
  # Right now the loss is a sum over all training examples, but we want it
  # to be an average instead so we divide by num_train.
  loss /= num_train

  # average the gradients
  dW /= num_train

  # Add regularization to the loss.
  loss += 0.5 * reg * np.sum(W * W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  #pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_train = X.shape[0]

  scores = X.dot(W)
  scores -= np.max(scores)
  
  correct_class_scores = scores[np.arange(scores.shape[0]), y]
    
  loss = np.sum(-np.log(np.exp(correct_class_scores) / np.sum(np.exp(scores), 
                                                              axis=1)))
  
  # create intermediate derivative matrix and -1 for each correct class score
  dW_int = np.exp(scores) / np.sum(np.exp(scores), axis=1)[:,np.newaxis]
  dW_int[np.arange(scores.shape[0]), y] -= 1
  
  dW = np.dot(X.T, dW_int)

  # Right now the loss is a sum over all training examples, but we want it
  # to be an average instead so we divide by num_train.
  loss /= num_train 

  # average the gradients
  dW /= num_train

  # Add regularization to the loss.
  loss += 0.5 * reg * np.sum(W * W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

