#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: GSM Full-Rate 06.10 Codec Looback Test
# Author: Martin Braun
# Description: An example how to use the GSM-FR Vocoder
# Generated: Mon May  1 22:28:32 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import vocoder
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class loopback_gsmfr(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "GSM Full-Rate 06.10 Codec Looback Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("GSM Full-Rate 06.10 Codec Looback Test")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "loopback_gsmfr")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.scale = scale = 2**12
        self.samp_rate = samp_rate = 48000
        self.play_encoded = play_encoded = True

        ##################################################
        # Blocks
        ##################################################
        _play_encoded_check_box = Qt.QCheckBox('Encode Audio')
        self._play_encoded_choices = {True: 1, False: 0}
        self._play_encoded_choices_inv = dict((v,k) for k,v in self._play_encoded_choices.iteritems())
        self._play_encoded_callback = lambda i: Qt.QMetaObject.invokeMethod(_play_encoded_check_box, "setChecked", Qt.Q_ARG("bool", self._play_encoded_choices_inv[i]))
        self._play_encoded_callback(self.play_encoded)
        _play_encoded_check_box.stateChanged.connect(lambda i: self.set_play_encoded(self._play_encoded_choices[bool(i)]))
        self.top_layout.addWidget(_play_encoded_check_box)
        self.vocoder_gsm_fr_encode_sp_1 = vocoder.gsm_fr_encode_sp()
        self.vocoder_gsm_fr_decode_ps_0 = vocoder.gsm_fr_decode_ps()
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=2,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=2,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	8000, #samp_rate
        	'Audio Pre-Encoding', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	8000, #samp_rate
        	'Audio Post-Encoding', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_char*1, 33)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_char*1, 33)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, scale)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, scale)
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=play_encoded,
        	output_index=0,
        )
        self.audio_source_0 = audio.source(16000, '', True)
        self.audio_sink_0 = audio.sink(16000, '', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.audio_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blks2_selector_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.vocoder_gsm_fr_encode_sp_1, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blks2_selector_0, 1))
        self.connect((self.blocks_short_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.vocoder_gsm_fr_decode_ps_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blks2_selector_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_float_to_short_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.audio_sink_0, 0))
        self.connect((self.vocoder_gsm_fr_decode_ps_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.vocoder_gsm_fr_encode_sp_1, 0), (self.blocks_vector_to_stream_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "loopback_gsmfr")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_scale(self):
        return self.scale

    def set_scale(self, scale):
        self.scale = scale
        self.blocks_short_to_float_0.set_scale(self.scale)
        self.blocks_float_to_short_0.set_scale(self.scale)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_play_encoded(self):
        return self.play_encoded

    def set_play_encoded(self, play_encoded):
        self.play_encoded = play_encoded
        self._play_encoded_callback(self.play_encoded)
        self.blks2_selector_0.set_input_index(int(self.play_encoded))


def main(top_block_cls=loopback_gsmfr, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
