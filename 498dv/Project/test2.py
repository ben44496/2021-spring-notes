#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: ben44496
# GNU Radio version: 3.9.4.0

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
from gnuradio import blocks
from gnuradio import digital
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time



from gnuradio import qtgui

class test2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("GNU Radio", "test2")

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
        self.sync_word2 = sync_word2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.sync_word1 = sync_word1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.samp_rate = samp_rate = 32000
        self.fft_len = fft_len = 64

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_source_0.set_center_freq(0, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.fft_vxx_1 = fft.fft_vcc(64, True, window.blackmanharris(1024), True, 1)
        self.fft_vxx_0 = fft.fft_vcc(64, True, window.blackmanharris(1024), True, 1)
        self.digital_packet_headerparser_b_0 = digital.packet_headerparser_b()
        self.digital_ofdm_sync_sc_cfb_0 = digital.ofdm_sync_sc_cfb(64, 16, False, 0.9)
        self.digital_ofdm_serializer_vcc_1 = digital.ofdm_serializer_vcc(fft_len, , '', "", 0, "", True)
        self.digital_ofdm_serializer_vcc_0 = digital.ofdm_serializer_vcc(fft_len, , '', "", 0, "", True)
        self.digital_ofdm_frame_equalizer_vcvc_1 = digital.ofdm_frame_equalizer_vcvc(, 16, '', True, 0)
        self.digital_ofdm_frame_equalizer_vcvc_0 = digital.ofdm_frame_equalizer_vcvc(, 16, '', True, 0)
        self.digital_ofdm_chanest_vcvc_0 = digital.ofdm_chanest_vcvc(sync_word1, sync_word2, 1, 0, 3, False)
        self.digital_header_payload_demux_0 = digital.header_payload_demux(
            3,
            64,
            0,
            "frame_len",
            "",
            False,
            gr.sizeof_gr_complex,
            "rx_time",
            samp_rate,
            ,
            0)
        self.digital_crc32_bb_0 = digital.crc32_bb(True, "packet_len", True)
        self.digital_constellation_decoder_cb_1 = digital.constellation_decoder_cb()
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb()
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_char*1, 'Rx Bytes', "")
        self.blocks_tag_debug_0.set_display(True)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(2, 8, "", False, gr.GR_LSB_FIRST)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 80)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(-31.25)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.digital_packet_headerparser_b_0, 'header_data'), (self.digital_header_payload_demux_0, 'header_data'))
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.digital_header_payload_demux_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_crc32_bb_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.digital_constellation_decoder_cb_1, 0), (self.digital_packet_headerparser_b_0, 0))
        self.connect((self.digital_crc32_bb_0, 0), (self.blocks_tag_debug_0, 0))
        self.connect((self.digital_header_payload_demux_0, 1), (self.fft_vxx_0, 0))
        self.connect((self.digital_header_payload_demux_0, 0), (self.fft_vxx_1, 0))
        self.connect((self.digital_ofdm_chanest_vcvc_0, 0), (self.digital_ofdm_frame_equalizer_vcvc_1, 0))
        self.connect((self.digital_ofdm_frame_equalizer_vcvc_0, 0), (self.digital_ofdm_serializer_vcc_0, 0))
        self.connect((self.digital_ofdm_frame_equalizer_vcvc_1, 0), (self.digital_ofdm_serializer_vcc_1, 0))
        self.connect((self.digital_ofdm_serializer_vcc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_ofdm_serializer_vcc_1, 0), (self.digital_constellation_decoder_cb_1, 0))
        self.connect((self.digital_ofdm_sync_sc_cfb_0, 0), (self.analog_frequency_modulator_fc_0, 0))
        self.connect((self.digital_ofdm_sync_sc_cfb_0, 1), (self.digital_header_payload_demux_0, 1))
        self.connect((self.fft_vxx_0, 0), (self.digital_ofdm_frame_equalizer_vcvc_0, 0))
        self.connect((self.fft_vxx_1, 0), (self.digital_ofdm_chanest_vcvc_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.digital_ofdm_sync_sc_cfb_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "test2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sync_word2(self):
        return self.sync_word2

    def set_sync_word2(self, sync_word2):
        self.sync_word2 = sync_word2

    def get_sync_word1(self):
        return self.sync_word1

    def set_sync_word1(self, sync_word1):
        self.sync_word1 = sync_word1

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len




def main(top_block_cls=test2, options=None):

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
