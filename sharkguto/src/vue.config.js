#!/usr/bin/env node
/**
 * @File   : vue.config.js
 * @Author : Gustavo Freitas (gustavo@gmf-tech.com)
 * @Link   :
 * @Date   : 10/21/2019, 8:58:40 AM
 */


module.exports = {
  configureWebpack: {
    optimization: {
      splitChunks: false,
    },
  },
};
