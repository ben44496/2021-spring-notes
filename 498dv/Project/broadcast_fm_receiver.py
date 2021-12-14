#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Broadcast FM receiver
# Author: ben44496
# GNU Radio version: v3.10-compat-xxx-xunknown

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class broadcast_fm_receiver(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Broadcast FM receiver", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Broadcast FM receiver")
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

        self.settings = Qt.QSettings("GNU Radio", "broadcast_fm_receiver")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 300e-3
        self.tuning = tuning = 102.1e6
        self.samp_rate = samp_rate = 1.92e6
        self.rf_decim = rf_decim = 10
        self.interp = interp = 1
        self.deviation = deviation = 75e3
        self.audio_decim = audio_decim = 4

        ##################################################
        # Blocks
        ##################################################
        self._volume_range = Range(0, 1, 50e-3, 300e-3, 200)
        self._volume_win = RangeWidget(self._volume_range, self.set_volume, 'Volume', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._volume_win)
        self._tuning_range = Range(88e6, 108e6, 200e3, 102.1e6, 200)
        self._tuning_win = RangeWidget(self._tuning_range, self.set_tuning, 'Frequency', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._tuning_win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        # No synchronization enforced.

        self.uhd_usrp_source_0.set_center_freq(tuning, 0)
        self.uhd_usrp_source_0.set_antenna('AB', 0)
        self.uhd_usrp_source_0.set_bandwidth(500e3, 0)
        self.uhd_usrp_source_0.set_rx_agc(True, 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=rf_decim,
                taps=[],
                fractional_bw=0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(volume)
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_fm_demod_cf_0 = analog.fm_demod_cf(
        	channel_rate=192e3,
        	audio_decim=audio_decim,
        	deviation=75000,
        	audio_pass=16000,
        	audio_stop=20000,
        	gain=1.0,
        	tau=75e-6,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fm_demod_cf_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_fm_demod_cf_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.rational_resampler_xxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "broadcast_fm_receiver")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k(self.volume)

    def get_tuning(self):
        return self.tuning

    def set_tuning(self, tuning):
        self.tuning = tuning
        self.uhd_usrp_source_0.set_center_freq(self.tuning, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_rf_decim(self):
        return self.rf_decim

    def set_rf_decim(self, rf_decim):
        self.rf_decim = rf_decim

    def get_interp(self):
        return self.interp

    def set_interp(self, interp):
        self.interp = interp

    def get_deviation(self):
        return self.deviation

    def set_deviation(self, deviation):
        self.deviation = deviation

    def get_audio_decim(self):
        return self.audio_decim

    def set_audio_decim(self, audio_decim):
        self.audio_decim = audio_decim




def main(top_block_cls=broadcast_fm_receiver, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
