(self["webpackChunkkatscript_jupyterlab"] = self["webpackChunkkatscript_jupyterlab"] || []).push([["lib_index_js"],{

/***/ "./lib/codemirror-katscript-python.js":
/*!********************************************!*\
  !*** ./lib/codemirror-katscript-python.js ***!
  \********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "setupKatScriptCodeMirror": () => (/* binding */ setupKatScriptCodeMirror)
/* harmony export */ });
/* harmony import */ var _codemirror_my_multiplex__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./codemirror-my-multiplex */ "./lib/codemirror-my-multiplex.js");
/* harmony import */ var _codemirror_katscript2__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./codemirror-katscript2 */ "./lib/codemirror-katscript2.js");
/* harmony import */ var _codemirror_katscript__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./codemirror-katscript */ "./lib/codemirror-katscript.js");



function setupKatScriptCodeMirror(codemirror) {
    const cm = codemirror.CodeMirror;
    (0,_codemirror_my_multiplex__WEBPACK_IMPORTED_MODULE_0__.defineMultiplexingMode)(codemirror);
    (0,_codemirror_katscript2__WEBPACK_IMPORTED_MODULE_1__.defineKatScript2Mode)(codemirror);
    (0,_codemirror_katscript__WEBPACK_IMPORTED_MODULE_2__.defineKatScriptMode)(codemirror);
    cm.defineMode('katscript-python', (config) => {
        const pmode = cm.getMode(config, 'python');
        return cm.myMultiplexingMode(pmode, {
            open: /(?=#kat2)/,
            close: /(?=""")/,
            mode: cm.getMode(config, 'text/x-katscript2'),
            delimStyle: 'delim',
        }, {
            open: /(?=#kat)/,
            close: /(?=""")/,
            mode: cm.getMode(config, 'text/x-katscript'),
            delimStyle: 'delim',
        });
    });
    cm.defineMIME('text/x-katscript-python', 'katscript-python');
    cm.modeInfo.push({
        name: 'KatScript Python',
        mime: 'text/x-katscript-python',
        mode: 'katscript-python',
        ext: [],
    });
}


/***/ }),

/***/ "./lib/codemirror-katscript-types.js":
/*!*******************************************!*\
  !*** ./lib/codemirror-katscript-types.js ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "commands": () => (/* binding */ commands),
/* harmony export */   "elements": () => (/* binding */ elements),
/* harmony export */   "functions": () => (/* binding */ functions),
/* harmony export */   "keywords": () => (/* binding */ keywords),
/* harmony export */   "operators": () => (/* binding */ operators)
/* harmony export */ });
const commands = ['opt_rf_readout_phase',
    'propagate_beam_astig',
    'frequency_response',
    'sensing_matrix_dc',
    'noise_projection',
    'print_model_attr',
    'noise_analysis',
    'propagate_beam',
    'print_model',
    'beam_trace',
    'run_locks',
    'freqresp',
    'parallel',
    'noxaxis',
    'change',
    'intrix',
    'lambda',
    'series',
    'x2axis',
    'x3axis',
    'debug',
    'modes',
    'print',
    'sweep',
    'xaxis',
    'abcd',
    'fsig',
    'link',
    'plot',
    'tem'];
const elements = ['quantum_shot_noise_detector_demod_1',
    'quantum_shot_noise_detector_demod_2',
    'quantum_noise_detector_demod_1',
    'quantum_noise_detector_demod_2',
    'quantum_shot_noise_detector',
    'directional_beamsplitter',
    'beam_property_detector',
    'power_detector_demod_1',
    'power_detector_demod_2',
    'quantum_noise_detector',
    'amplitude_detector',
    'degree_of_freedom',
    'power_detector_dc',
    'optical_bandpass',
    'signal_generator',
    'motion_detector',
    'readout_dc_qpd',
    'filter_butter',
    'filter_cheby1',
    'beamsplitter',
    'zpk_actuator',
    'ligo_triple',
    'filter_zpk',
    'readout_dc',
    'readout_rf',
    'amplifier',
    'free_mass',
    'ligo_quad',
    'modulator',
    'actuator',
    'isolator',
    'pendulum',
    'qnoised1',
    'qnoised2',
    'squeezer',
    'variable',
    'ccdline',
    'nothing',
    'qnoised',
    'splitpd',
    'astigd',
    'butter',
    'cavity',
    'cheby1',
    'mirror',
    'qshot1',
    'qshot2',
    'ccdpx',
    'fline',
    'gauss',
    'laser',
    'noise',
    'qshot',
    'space',
    'fcam',
    'gouy',
    'isol',
    'knmd',
    'lens',
    'lock',
    'sgen',
    'amp',
    'cav',
    'ccd',
    'dbs',
    'dof',
    'fpx',
    'mmd',
    'mod',
    'obp',
    'pd1',
    'pd2',
    'var',
    'zpk',
    'ad',
    'bp',
    'bs',
    'cp',
    'pd',
    'sq',
    'xd',
    'l',
    'm',
    's'];
const functions = ['geomspace',
    'linspace',
    'logspace',
    'arctan2',
    'deg2rad',
    'degrees',
    'rad2deg',
    'radians',
    'arccos',
    'arcsin',
    'conj',
    'imag',
    'real',
    'sqrt',
    'abs',
    'cos',
    'exp',
    'neg',
    'pos',
    'sin',
    'tan'];
const keywords = ['resolution',
    'stability',
    'bandpass',
    'bandstop',
    'highpass',
    'finesse',
    'lowpass',
    'modesep',
    'length',
    'xsplit',
    'ysplit',
    'abcd',
    'even',
    'fwhm',
    'gouy',
    'loss',
    'none',
    'pole',
    'div',
    'fsr',
    'lin',
    'log',
    'odd',
    'off',
    'tau',
    'am',
    'c0',
    'pi',
    'pm',
    'rc',
    'w0',
    'zr',
    'g',
    'l',
    'q',
    's',
    'w',
    'x',
    'y',
    'z'];
const operators = ['+', '/', '*', '&', '-'];


/***/ }),

/***/ "./lib/codemirror-katscript.js":
/*!*************************************!*\
  !*** ./lib/codemirror-katscript.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "defineKatScriptMode": () => (/* binding */ defineKatScriptMode)
/* harmony export */ });
/* harmony import */ var _codemirror_katscript_types__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./codemirror-katscript-types */ "./lib/codemirror-katscript-types.js");

const booleans = ['True', 'true', 'False', 'false'];
function wordListRegexp(words) {
    return new RegExp('((' + words.join(')|(') + '))');
}
function symbolListRegexp(words) {
    return new RegExp('[' + words.join('') + ']');
}
function fullString(re) {
    return new RegExp('^' + re.source + '$');
}
const regex = {
    command: wordListRegexp(_codemirror_katscript_types__WEBPACK_IMPORTED_MODULE_0__.commands),
    fullcommand: fullString(wordListRegexp(_codemirror_katscript_types__WEBPACK_IMPORTED_MODULE_0__.commands)),
    element: wordListRegexp(_codemirror_katscript_types__WEBPACK_IMPORTED_MODULE_0__.elements),
    fullelement: fullString(wordListRegexp(_codemirror_katscript_types__WEBPACK_IMPORTED_MODULE_0__.elements)),
    function: wordListRegexp(_codemirror_katscript_types__WEBPACK_IMPORTED_MODULE_0__.functions),
    fullfunction: fullString(wordListRegexp(_codemirror_katscript_types__WEBPACK_IMPORTED_MODULE_0__.functions)),
    keyword: wordListRegexp(_codemirror_katscript_types__WEBPACK_IMPORTED_MODULE_0__.keywords),
    fullkeyword: fullString(wordListRegexp(_codemirror_katscript_types__WEBPACK_IMPORTED_MODULE_0__.keywords)),
    operator: symbolListRegexp(_codemirror_katscript_types__WEBPACK_IMPORTED_MODULE_0__.operators),
    name: /[a-zA-Z_][a-zA-Z0-9._-]*/,
    number: /(([+-]?inf)|([+-]?(\d+\.\d*|\d*\.\d+|\d+)([eE]-?\d*\.?\d*)?j?([pnumkMGT])?))/,
    boolean: wordListRegexp(booleans),
    fullboolean: fullString(wordListRegexp(booleans)),
    bracket: /[()]/,
};
/*
 * Available tokens:
 *
 * keyword
 * atom
 * number
 * def
 * variable
 * variable-2
 * variable-3
 * property
 * operator
 * comment
 * string
 * string-2
 * meta
 * qualifier
 * builtin
 * bracket
 * tag
 * attribute
 * header
 * quote
 * hr
 * link
 */
function defineKatScriptMode(codemirror) {
    const cm = codemirror.CodeMirror;
    cm.defineMode('katscript', () => {
        function tokenBase(stream, state) {
            // Give each line a slight background, to differentiate from Python code.
            return 'line-background-katscript ' + tokenLex(stream, state);
        }
        function tokenLex(stream, state) {
            if (stream.sol()) {
                state.firstOnLine = true;
            }
            // Skip to the next non-space character
            if (stream.eatSpace()) {
                return;
            }
            // If it's a comment, skip the rest of the line
            if (/#/.test(stream.peek())) {
                stream.skipToEnd();
                return 'comment';
            }
            // Strings can be either single or double quoted, and quotes can be
            // escaped inside them
            if (/["']/.test(stream.peek())) {
                const char = stream.next();
                const re = RegExp('[^' + char + ']');
                stream.eatWhile(re);
                let cur = stream.current();
                while (cur[cur.length - 1] === '\\') {
                    if (!stream.next()) {
                        break;
                    }
                    stream.eatWhile(re);
                    cur = stream.current();
                }
                stream.eat(char);
                return 'string';
            }
            let style = null;
            if (state.firstOnLine) {
                // Only check for component definitions and commands at the start of
                // the line.
                if (stream.match(regex['element']) || stream.match(regex['command'])) {
                    // Some elements can be substrings of commands, and vice versa e.g.
                    // "l" (element) and "link" (command). To choose the correct one, we
                    // first continue grabbing the rest of the current word (if there is
                    // any more), then test the entire word against element/command
                    // names.
                    stream.eatWhile(/\w/);
                    const cur = stream.current();
                    if (regex['fullelement'].test(cur)) {
                        // Component definition
                        style = 'variable-3';
                        state.nextIsDef = true;
                    }
                    else if (regex['fullcommand'].test(cur)) {
                        // Command
                        style = 'builtin';
                    }
                }
            }
            if (style === null) {
                if (state.nextIsDef && stream.match(regex['name'])) {
                    // Component name
                    style = 'def';
                    state.nextIsDef = false;
                }
                else if (stream.match(regex['keyword']) ||
                    stream.match(regex['boolean']) ||
                    stream.match(regex['function'])) {
                    // Same reasoning as before, grab the rest of the word then check the
                    // whole thing.
                    stream.eatWhile(/\w/);
                    const cur = stream.current();
                    if (regex['fullkeyword'].test(cur)) {
                        style = 'keyword';
                    }
                    else if (regex['fullboolean'].test(cur)) {
                        style = 'keyword';
                    }
                    else if (regex['fullfunction'].test(cur)) {
                        style = 'builtin';
                    }
                    else {
                        // We accidentally grabbed a variable.
                        style = 'variable';
                    }
                }
                else if (stream.match(regex['number'])) {
                    style = 'number';
                }
                else if (stream.match(regex['operator'])) {
                    style = 'operator';
                }
                else if (stream.match(regex['bracket'])) {
                    style = 'bracket';
                }
                else if (stream.match(regex['name'])) {
                    style = 'variable';
                }
            }
            if (style !== null) {
                state.firstOnLine = false;
                return style;
            }
            stream.next();
        }
        return {
            startState: function () {
                return {
                    tokenize: tokenBase,
                    firstOnLine: true,
                    nextIsDef: false,
                };
            },
            blankLine: function (state) {
                return 'line-background-katscript';
            },
            token: function (stream, state) {
                return state.tokenize(stream, state);
            },
        };
    });
    cm.defineMIME('text/x-katscript', 'katscript');
}


/***/ }),

/***/ "./lib/codemirror-katscript2.js":
/*!**************************************!*\
  !*** ./lib/codemirror-katscript2.js ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "defineKatScript2Mode": () => (/* binding */ defineKatScript2Mode)
/* harmony export */ });
const components = [
    'bs[12]?',
    'dbs',
    'grd*',
    'isol',
    'l',
    'lens',
    'm[12]?',
    'mod',
    's',
    'sq',
];
const detectors = [
    'ad',
    'beam',
    'bp',
    'cp',
    'guoy',
    'hd',
    'pd[SN]?d*',
    'pgaind',
    'qd',
    'qd*hd?',
    'qhd[SN]?',
    'qnoised[SN]?',
    'qshot',
    'qshot[SN]?',
    'sd',
    'xd',
];
const commands = [
    'attr',
    'cav',
    'conf',
    'fadd',
    'fsig',
    'gauss',
    'knm',
    'lambda',
    'map',
    'mask',
    'maxtem',
    'pdtype',
    'phase',
    'retrace',
    'smotion',
    'startnode',
    'tem',
    'tf2?',
    'vacuum',
    // Plotting:
    'const',
    'deriv_h',
    'diff',
    'func',
    'lock',
    'noplot',
    'noxaxis',
    'put',
    'scale',
    'set',
    'trace',
    'var',
    'x2?axis',
    'yaxis',
    // Auxiliary
    'gnuterm',
    'multi',
    'pause',
    'pyterm',
];
const reserved = ['dump'];
function wordListRegexp(words) {
    return new RegExp('^((' + words.join(')|(') + '))$');
}
const regex = {
    command: wordListRegexp(commands),
    component: wordListRegexp(components),
    detector: wordListRegexp(detectors),
    name: /[a-zA-Z_][a-zA-Z0-9_-]/,
    number: /^(([+-]?inf)|([+-]?(\d+\.\d*|\d*\.\d+|\d+)([eE]-?\d*\.?\d*)?j?([pnumkMGT])?))$/,
    reserved: wordListRegexp(reserved),
    variable: /\$\w+/,
};
/*
 * Available tokens:
 *
 * keyword
 * atom
 * number
 * def
 * variable
 * variable-2
 * variable-3
 * property
 * operator
 * comment
 * string
 * string-2
 * meta
 * qualifier
 * builtin
 * bracket
 * tag
 * attribute
 * header
 * quote
 * hr
 * link
 */
function defineKatScript2Mode(codemirror) {
    const cm = codemirror.CodeMirror;
    cm.defineMode('katscript2', () => {
        function tokenBase(stream, state) {
            return 'line-background-katscript ' + tokenLex(stream, state);
        }
        function tokenLex(stream, state) {
            if (stream.sol()) {
                state.firstOnLine = true;
            }
            if (stream.eatSpace()) {
                return;
            }
            if (/[#%]/.test(stream.peek())) {
                stream.skipToEnd();
                return 'comment';
            }
            if (stream.peek() === '$') {
                stream.next();
            }
            stream.eatWhile(/[^\s]/);
            let style = null;
            const cur = stream.current();
            if (state.firstOnLine) {
                if (regex['component'].test(cur) || regex['detector'].test(cur)) {
                    // Component definition
                    style = 'keyword';
                    state.nextIsDef = true;
                }
                else if (regex['command'].test(cur)) {
                    // Command
                    style = 'builtin';
                }
            }
            else if (state.nextIsDef && regex['name'].test(cur)) {
                // Component name
                style = 'def';
                state.nextIsDef = false;
            }
            else if (regex['number'].test(cur)) {
                // Number
                style = 'number';
            }
            else if (regex['reserved'].test(cur)) {
                // Reserved keyword
                style = 'keyword';
            }
            else if (regex['variable'].test(cur)) {
                style = 'variable-2';
            }
            if (style !== null) {
                state.firstOnLine = false;
                return style;
            }
            stream.next();
        }
        return {
            startState: function () {
                return {
                    tokenize: tokenBase,
                    firstOnLine: true,
                    nextIsDef: false,
                };
            },
            blankLine: function (state) {
                return 'line-background-katscript';
            },
            token: function (stream, state) {
                return state.tokenize(stream, state);
            },
        };
    });
    cm.defineMIME('text/x-katscript2', 'katscript2');
}


/***/ }),

/***/ "./lib/codemirror-my-multiplex.js":
/*!****************************************!*\
  !*** ./lib/codemirror-my-multiplex.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "defineMultiplexingMode": () => (/* binding */ defineMultiplexingMode)
/* harmony export */ });
// CodeMirror, copyright (c) by Marijn Haverbeke and others
// Distributed under an MIT license: https://codemirror.net/LICENSE
//
// This is a clone of addon/mode/multiplexingMode.js from CodeMirror. The
// original blankLine function doesn't return the style returned by its
// sub-modes, so we have to copy the whole thing in here -_-

function defineMultiplexingMode(codemirror) {
  const cm = codemirror.CodeMirror;
  cm.myMultiplexingMode = function (outer /*, others */) {
    // Others should be {open, close, mode [, delimStyle] [, innerStyle]} objects
    var others = Array.prototype.slice.call(arguments, 1);

    function indexOf(string, pattern, from, returnEnd) {
      if (typeof pattern == 'string') {
        var found = string.indexOf(pattern, from);
        return returnEnd && found > -1 ? found + pattern.length : found;
      }
      var m = pattern.exec(from ? string.slice(from) : string);
      return m ? m.index + from + (returnEnd ? m[0].length : 0) : -1;
    }

    return {
      startState: function () {
        return {
          outer: cm.startState(outer),
          innerActive: null,
          inner: null,
          startingInner: false
        };
      },

      copyState: function (state) {
        return {
          outer: cm.copyState(outer, state.outer),
          innerActive: state.innerActive,
          inner:
            state.innerActive &&
            cm.copyState(state.innerActive.mode, state.inner),
          startingInner: state.startingInner
        };
      },

      token: function (stream, state) {
        if (!state.innerActive) {
          var cutOff = Infinity,
            oldContent = stream.string;
          for (var i = 0; i < others.length; ++i) {
            var other = others[i];
            var found = indexOf(oldContent, other.open, stream.pos);
            if (found == stream.pos) {
              if (!other.parseDelimiters) stream.match(other.open);
              state.startingInner = !!other.parseDelimiters;
              state.innerActive = other;

              // Get the outer indent, making sure to handle cm.Pass
              var outerIndent = 0;
              if (outer.indent) {
                var possibleOuterIndent = outer.indent(state.outer, '', '');
                if (possibleOuterIndent !== cm.Pass)
                  outerIndent = possibleOuterIndent;
              }

              state.inner = cm.startState(other.mode, outerIndent);
              return (
                other.delimStyle &&
                other.delimStyle + ' ' + other.delimStyle + '-open'
              );
            } else if (found != -1 && found < cutOff) {
              cutOff = found;
            }
          }
          if (cutOff != Infinity) stream.string = oldContent.slice(0, cutOff);
          var outerToken = outer.token(stream, state.outer);
          if (cutOff != Infinity) stream.string = oldContent;
          return outerToken;
        } else {
          var curInner = state.innerActive,
            oldContent = stream.string;
          if (!curInner.close && stream.sol()) {
            state.innerActive = state.inner = null;
            return this.token(stream, state);
          }
          var found =
            curInner.close && !state.startingInner
              ? indexOf(
                  oldContent,
                  curInner.close,
                  stream.pos,
                  curInner.parseDelimiters
                )
              : -1;
          if (found == stream.pos && !curInner.parseDelimiters) {
            stream.match(curInner.close);
            state.innerActive = state.inner = null;
            return (
              curInner.delimStyle &&
              curInner.delimStyle + ' ' + curInner.delimStyle + '-close'
            );
          }
          if (found > -1) stream.string = oldContent.slice(0, found);
          var innerToken = curInner.mode.token(stream, state.inner);
          if (found > -1) stream.string = oldContent;
          else if (stream.pos > stream.start) state.startingInner = false;

          if (found == stream.pos && curInner.parseDelimiters)
            state.innerActive = state.inner = null;

          if (curInner.innerStyle) {
            if (innerToken) innerToken = innerToken + ' ' + curInner.innerStyle;
            else innerToken = curInner.innerStyle;
          }

          return innerToken;
        }
      },

      indent: function (state, textAfter, line) {
        var mode = state.innerActive ? state.innerActive.mode : outer;
        if (!mode.indent) return cm.Pass;
        return mode.indent(
          state.innerActive ? state.inner : state.outer,
          textAfter,
          line
        );
      },

      blankLine: function (state) {
        var mode = state.innerActive ? state.innerActive.mode : outer;
        var ret = null;
        if (mode.blankLine) {
          ret = mode.blankLine(state.innerActive ? state.inner : state.outer);
        }
        if (!state.innerActive) {
          for (var i = 0; i < others.length; ++i) {
            var other = others[i];
            if (other.open === '\n') {
              state.innerActive = other;
              state.inner = cm.startState(
                other.mode,
                mode.indent ? mode.indent(state.outer, '', '') : 0
              );
            }
          }
        } else if (state.innerActive.close === '\n') {
          state.innerActive = state.inner = null;
        }
        return ret;
      },

      electricChars: outer.electricChars,

      innerMode: function (state) {
        return state.inner
          ? { state: state.inner, mode: state.innerActive.mode }
          : { state: state.outer, mode: outer };
      }
    };
  };
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/codemirror */ "webpack/sharing/consume/default/@jupyterlab/codemirror");
/* harmony import */ var _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/cells */ "webpack/sharing/consume/default/@jupyterlab/cells");
/* harmony import */ var _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _codemirror_katscript_python__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./codemirror-katscript-python */ "./lib/codemirror-katscript-python.js");




const plugin = {
    id: 'katscript-jupyter',
    autoStart: true,
    requires: [_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.INotebookTracker, _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_1__.ICodeMirror],
    activate,
};
function activate(app, tracker, codemirror) {
    (0,_codemirror_katscript_python__WEBPACK_IMPORTED_MODULE_3__.setupKatScriptCodeMirror)(codemirror);
    const style = document.createElement('style');
    style.type = 'text/css';
    style.innerHTML = '.katscript { background-color: rgba(0, 0, 0, 0.04); }';
    document.getElementsByTagName('head')[0].appendChild(style);
    tracker.widgetAdded.connect(activate_katscript);
}
function check_all(sender) {
    sender.content.widgets.forEach(cell => {
        if (cell instanceof _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__.CodeCell &&
            cell.model.mimeType !== 'text/x-katscript-python') {
            cell.model.mimeType = 'text/x-katscript-python';
        }
    });
}
function set_mime(model) {
    // Jupyter seems to have some weirdness related to setup of the
    // mime type of each cell. To avoid having timeouts everywhere,
    // everytime we select a new cell, we attach a function that checks the
    // mime type on each content change and sets it if required, otherwise
    // disconnects itself.
    if (model.mimeType === 'text/x-katscript-python') {
        model.contentChanged.disconnect(set_mime);
    }
    else {
        model.mimeType = 'text/x-katscript-python';
    }
}
function check_cell(sender, cell) {
    if (cell instanceof _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_2__.CodeCell) {
        cell.model.contentChanged.connect(set_mime);
    }
}
function activate_katscript(sender, panel) {
    panel.content.activeCellChanged.connect(check_cell);
    // I ain't proud of this, but it's the sanest way I could find to get
    // the syntax highlighting to change on startup without selecting a
    // different cell
    setTimeout(() => {
        check_all(panel);
    }, 500);
    setTimeout(() => {
        check_all(panel);
    }, 2000);
    setTimeout(() => {
        check_all(panel);
    }, 5000);
}
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.b8b304e116fe498155ca.js.map