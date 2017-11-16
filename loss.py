import tensorflow as tf


def gan_loss(logits_real, logits_fake):
    """Compute the GAN loss.

    Inputs:
    - logits_real: Tensor, shape [batch_size, 1], output of discriminator
        Log probability that the image is real for each real image
    - logits_fake: Tensor, shape[batch_size, 1], output of discriminator
        Log probability that the image is real for each fake image

    Returns:
    - D_loss: discriminator loss scalar
    - G_loss: generator loss scalar
    """
    # TODO: compute D_loss and G_loss
    labels_ones_f = tf.ones_like(logits_fake)
    labels_zeros_f = tf.zeros_like(logits_fake)
    labels_ones_r = tf.ones_like(logits_real)
    G_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=labels_ones_f, logits=logits_fake))
    D_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=labels_ones_r, logits=logits_real))
    D_loss += tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=labels_zeros_f, logits=logits_fake))

    return D_loss, G_loss


def lsgan_loss(logits_real, logits_fake):
    """Compute the Least Squares GAN loss.
    """
    # TODO: compute D_loss and G_loss
    D_loss = tf.reduce_mean(tf.square(logits_real - 1)) + tf.reduce_mean(tf.square(logits_fake))
    G_loss = tf.reduce_mean(tf.square(logits_fake - 1))
    D_loss /= 2
    G_loss /= 2
    return D_loss, G_loss


def l1_loss(real, fake):
    return tf.reduce_mean(tf.abs(real - fake))
